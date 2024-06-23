class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        m, n = len(matrix), len(matrix[0])
        cache = [[-1] * n for _ in range(m)]

        def dfs(x, y):
            if cache[x][y] != -1:
                return cache[x][y]

            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            max_length = 1

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and matrix[nx][ny] > matrix[x][y]:
                    length = 1 + dfs(nx, ny)
                    max_length = max(max_length, length)

            cache[x][y] = max_length
            return max_length

        max_path = 0
        for i in range(m):
            for j in range(n):
                max_path = max(max_path, dfs(i, j))

        return max_path