class Solution:
        def findBall(self, grid):
            nrows = len(grid)
            ncols = len(grid[0])
            def candrop(i,j):
                if i == nrows: return j
                if j == ncols-1 and grid[i][j] == 1: return -1
                if j == 0 and grid[i][j] == -1: return -1
                if grid[i][j] == 1 and grid[i][j+1] == -1: return -1
                if grid[i][j] == -1 and grid[i][j-1] == 1: return -1
                return candrop(i+1,j+grid[i][j])

            return [candrop(0,j) for j in range(ncols)]