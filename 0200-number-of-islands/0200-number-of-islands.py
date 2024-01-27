class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        ROWS = len(grid)
        COLS = len(grid[0])
        
        islands = 0
        visited = set() # [(r, c)]
        
        def dfs(row, column):
            if(
                row not in range(ROWS) 
                or
                column not in range(COLS)
                or 
                grid[row][column] == "0"
                or 
                (row, column) in visited
                ):
                return
            
            visited.add((row, column))
            
            directions = [[0,1],[0,-1],[1,0],[-1,0]]
            
            for rowdirection, coldirection in directions:
                dfs(row + rowdirection, column + coldirection)
            
        for row in range(ROWS):
            for column in range(COLS):
                if grid[row][column] == "1" and (row, column) not in visited:
                    islands += 1
                    dfs(row, column)
                    
        
        
        return islands
            
            
            