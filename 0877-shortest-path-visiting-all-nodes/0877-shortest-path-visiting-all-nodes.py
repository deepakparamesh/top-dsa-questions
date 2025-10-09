class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
    
        # Edge case: empty or single node graph
        if n <= 1:
            return 0
        
        # Target bitmask when all nodes are visited
        # For n=4: target = 1111 (binary) = 15 (decimal)
        target_mask = (1 << n) - 1
        
        # BFS queue: (current_node, visited_bitmask, distance)
        queue = deque()
        
        # Set to track visited states: (node, bitmask)
        # This prevents revisiting the same state
        visited = set()
        
        # Initialize: can start from any node
        for i in range(n):
            # Set bit i to 1 (mark node i as visited)
            mask = 1 << i
            queue.append((i, mask, 0))
            visited.add((i, mask))
        
        # BFS to find shortest path
        while queue:
            node, mask, dist = queue.popleft()
            
            # Check if all nodes have been visited
            if mask == target_mask:
                return dist
            
            # Explore all neighbors
            for neighbor in graph[node]:
                # Update bitmask by visiting neighbor
                new_mask = mask | (1 << neighbor)
                
                # If this state hasn't been visited
                if (neighbor, new_mask) not in visited:
                    visited.add((neighbor, new_mask))
                    queue.append((neighbor, new_mask, dist + 1))
        
        # Should never reach here for a connected graph
        return -1