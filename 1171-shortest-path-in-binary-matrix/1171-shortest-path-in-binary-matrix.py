class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
    
        # Check if path is possible
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1
        
        if n == 1:
            return 1
        
        # 8-directional movements
        directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
        
        # BFS
        queue = deque([(0, 0, 1)])
        grid[0][0] = 1  # Mark as visited by setting to 1
        
        while queue:
            row, col, dist = queue.popleft()
            
            # Try all 8 directions
            for dr, dc in directions:
                r, c = row + dr, col + dc
                
                # If we reached the destination
                if r == n-1 and c == n-1:
                    return dist + 1
                
                # If valid and unvisited
                if 0 <= r < n and 0 <= c < n and grid[r][c] == 0:
                    grid[r][c] = 1  # Mark as visited
                    queue.append((r, c, dist + 1))
        
        return -1