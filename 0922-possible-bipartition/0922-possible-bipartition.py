class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        
        from collections import defaultdict, deque

        graph = defaultdict(list)
        for a,b in dislikes:
            graph[a].append(b)
            graph[b].append(a)
        
        colors = [-1] * (n+1)

        def bfs(start):

            queue = deque([start])
            colors[start] = 0

            while queue:
                person = queue.popleft()
                current_color = colors[person]

                for disliked in graph[person]:
                    if colors[disliked] == -1:
                        colors[disliked] = 1 - current_color
                        queue.append(disliked)
                    elif colors[disliked] == current_color:
                        return False
            
            return True
        
        for person in range(1, n+1):
            if colors[person] == -1:
                if not bfs(person):
                    return False
        
        return True