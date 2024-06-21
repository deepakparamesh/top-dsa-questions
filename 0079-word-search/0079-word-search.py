class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        if not board or not board[0]:
            return False
        
        rows, cols = len(board), len(board[0])
        directions=[(0,1),(1,0),(0,-1),(-1,0)]
        def dfs(r, c, idx):
            if idx == len(word):
                return True
            
            if r < 0 or r >= rows or c <0 or c>=cols or board[r][c] != word[idx]:
                return False
            
            temp, board[r][c] = board[r][c], "#"
            for dr, dc in directions:
                if dfs(r + dr, c+dc, idx +1):
                    return True
            
            board[r][c] = temp
            return False
        
        for row in range(rows):
            for col in range(cols):
                if dfs(row, col,0):
                    return True
        
        return False
        
        