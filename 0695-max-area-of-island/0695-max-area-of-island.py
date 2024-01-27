class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid: 
            return 0
        
        visited = set()
        ROWS = len(grid)
        COLS = len(grid[0])
        
        def dfs(row, column):
            # base condition
            if( 
               row not in range(ROWS)
               or 
               column not in range(COLS)
               or
               grid[row][column] == 0
               or 
               (row, column) in visited 
               ):
                return 0
            
            # core logic
            visited.add((row, column))
            
            # traversal
            left = dfs(row-1, column)
            right = dfs(row+1, column)
            top = dfs(row, column+1)
            bottom = dfs(row, column-1)
            
            # dfs return
            return 1 + left + right + top + bottom
        
        area = 0
        for row in range(ROWS):
            for column in range(COLS):
                # we should not make this check. But in number of island we should
                # if grid[row][column] == "1" and (row, column) not in visited:
                    area = max(area, dfs(row, column))
        
        
        
        return area