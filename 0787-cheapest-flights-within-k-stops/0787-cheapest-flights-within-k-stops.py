class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Initialize distances array
        distances = [float('inf')] * n
        distances[src] = 0

        # Bellman-Ford algorithm for up to k stops
        for _ in range(k + 1):
            new_distances = distances[:]
            for u, v, w in flights:
                if distances[u] != float('inf'):
                    new_distances[v] = min(new_distances[v], distances[u] + w)
            distances = new_distances

        return distances[dst] if distances[dst] != float('inf') else -1