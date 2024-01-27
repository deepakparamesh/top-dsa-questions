class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid: 
            return 0
        
        visited = set()
        ROWS = len(grid)
        COLS = len(grid[0])
        
        def dfs(row, column):
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

            visited.add((row, column))
            
            
            # directions = [[0,1],[0,-1],[1,0],[-1,0]]
            # for rowDirection, colDirection in directions:
            return 1 + dfs(row + 1, column) + dfs(row - 1, column) + dfs(row, column + 1) + dfs(row, column - 1)
        
        area = 0
        for row in range(ROWS):
            for column in range(COLS):
               # if grid[row][column] == "1" and (row, column) not in visited:
                area = max(area, dfs(row, column))
        
        
        
        return area