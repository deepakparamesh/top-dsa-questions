class Solution:
    def maximalPathQuality(self, values: List[int], edges: List[List[int]], maxTime: int) -> int:
        
        graph = defaultdict(list)

        for u,v, time in edges:
            graph[u].append((v, time))
            graph[v].append((u, time))

        max_quality = 0
        visited = set()

        def dfs(node, current_time, current_quality):
            nonlocal max_quality

            if node == 0:
                max_quality = max(max_quality, current_quality)

            for neighbor, time_cost in graph[node]:
                if current_time + time_cost <= maxTime:
                    new_visited = False
                    if neighbor not in visited:
                        visited.add(neighbor)
                        new_visited = True
                        current_quality += values[neighbor]
                    
                    dfs(neighbor, current_time + time_cost, current_quality)

                    if new_visited:
                        visited.remove(neighbor)
                        current_quality -= values[neighbor]
            
        visited.add(0)
        dfs(0,0,values[0])

        return max_quality
