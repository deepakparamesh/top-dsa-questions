class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def is_safe(board, row, col):
            for i in range(row):
                if board[i][col] == 'Q':
                    return False
             
            i, j = row, col
            while i >= 0 and j >= 0:
                if board[i][j]=='Q':
                    return False
                
                i -= 1
                j -= 1
            
            i, j = row, col
            while i >= 0 and j < n:
                if board[i][j] == 'Q':
                    return False
                i-=1
                j+=1
            
            return True
            
            
        def solve(board, row):
            if row == n:
                result.append(["".join(row) for row in board])
                return
           
            for col in range(n):
                if is_safe(board, row, col):
                    board[row][col]='Q'
                    solve(board, row+1)
                    board[row][col] = '.'
        
        result = []
        board = [['.' for _ in range(n)]for _ in range(n)]
        solve(board, 0)
        
        return result