class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        if not board or not board[0]:
            return board
        
        rows, cols = len(board), len(board[0])
        click_row, click_col = click[0], click[1]
        
        # Boundary check - return unchanged if click is out of bounds
        if not (0 <= click_row < rows and 0 <= click_col < cols):
            return board
        
        # Get the clicked cell value
        clicked_cell = board[click_row][click_col]
        
        # Rule 1: If click on mine, reveal it and game over
        if clicked_cell == 'M':
            board[click_row][click_col] = 'X'
            return board
        
        # Rule 3: If already revealed (not 'E'), no change needed
        if clicked_cell != 'E':
            return board
        
        # Rule 2: Click on unrevealed empty square - use BFS to reveal area
        # Queue stores coordinates of cells to process
        queue = deque([(click_row, click_col)])
        
        # 8-directional movement vectors (including diagonals)
        directions = [
            (-1, -1), (-1, 0), (-1, 1),  # top row
            (0, -1),           (0, 1),   # middle row (excluding center)
            (1, -1),  (1, 0),  (1, 1)    # bottom row
        ]
        
        def count_adjacent_mines(row: int, col: int) -> int:
            """
            Count mines in all 8 adjacent cells around the given position.
            
            Args:
                row, col: Position to check around
                
            Returns:
                Number of adjacent mines (0-8)
            """
            mine_count = 0
            
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                
                # Check if neighbor is within bounds
                if 0 <= new_row < rows and 0 <= new_col < cols:
                    # Count both unrevealed mines ('M') and revealed mines ('X')
                    if board[new_row][new_col] in ['M', 'X']:
                        mine_count += 1
                        
            return mine_count
        
        def get_valid_neighbors(row: int, col: int) -> List[tuple]:
            """
            Get all valid unrevealed neighbor coordinates.
            
            Args:
                row, col: Center position
                
            Returns:
                List of (row, col) tuples for unrevealed neighbors
            """
            neighbors = []
            
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                
                # Check bounds and ensure cell is unrevealed
                if (0 <= new_row < rows and 0 <= new_col < cols and 
                    board[new_row][new_col] == 'E'):
                    neighbors.append((new_row, new_col))
                    
            return neighbors
        
        # BFS to reveal connected safe area
        while queue:
            current_row, current_col = queue.popleft()
            
            # Skip if already processed (might be added multiple times)
            if board[current_row][current_col] != 'E':
                continue
            
            # Count mines around current position
            adjacent_mines = count_adjacent_mines(current_row, current_col)
            
            if adjacent_mines > 0:
                # If there are adjacent mines, show the count
                board[current_row][current_col] = str(adjacent_mines)
                # Don't expand further from this cell
                
            else:
                # No adjacent mines - mark as blank and expand to neighbors
                board[current_row][current_col] = 'B'
                
                # Add all unrevealed neighbors to queue for processing
                neighbors = get_valid_neighbors(current_row, current_col)
                for neighbor_row, neighbor_col in neighbors:
                    queue.append((neighbor_row, neighbor_col))
        
        return board