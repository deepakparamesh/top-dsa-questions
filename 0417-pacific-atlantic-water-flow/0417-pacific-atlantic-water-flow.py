class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        if not heights or not heights[0]:
            return []
        
        m,n = len(heights), len(heights[0])

        pacific_reachable: Set[Tuple[int, int]] = set()
        atlantic_reachable: Set[Tuple[int, int]] = set()

        def dfs(row: int, col: int, visited:Set[Tuple[int, int]], prev_height: int) -> None:

            if(row <0 or row >= m or col < 0 or col >= n or 
            (row, col) in visited or
            heights[row][col] < prev_height):
                return

            visited.add((row, col))

            current_height = heights[row][col]
            directions =  [(-1,0), (1,0),(0,-1),(0,1)]


            for dr, dc in directions:
                next_row, next_col = row + dr, col + dc
                dfs(next_row, next_col, visited, current_height)
        
        for col in range(n):
            dfs(0, col, pacific_reachable, 0)
        
        for row in range(m):
            dfs(row, 0, pacific_reachable,0)
        
        for col in range(n):
            dfs(m-1, col, atlantic_reachable, 0)
        
        for row in range(m):
            dfs(row, n-1, atlantic_reachable, 0)
        
        result = []
        for row, col in pacific_reachable:
            if (row, col) in atlantic_reachable:
                result.append([row, col])
        
        return result




        