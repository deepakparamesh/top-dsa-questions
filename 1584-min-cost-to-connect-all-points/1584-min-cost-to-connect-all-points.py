class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def manhattan_dist(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
    
        n = len(points)
        if n == 0:
            return 0

        min_cost = 0
        visited = set()
        min_heap = [(0, 0)]  # (cost, point_index)

        while len(visited) < n:
            cost, i = heapq.heappop(min_heap)
            if i in visited:
                continue
            min_cost += cost
            visited.add(i)

            for j in range(n):
                if j not in visited:
                    heapq.heappush(min_heap, (manhattan_dist(points[i], points[j]), j))

        return min_cost