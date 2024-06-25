class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)
        
        task_counts = Counter(tasks)
        max_heap = [-count for count in task_counts.values()]
        heapq.heapify(max_heap)
        
        time = 0
        queue = deque()  # Queue to keep track of cooling tasks (time, count)
        
        while max_heap or queue:
            time += 1
            
            if max_heap:
                count = heapq.heappop(max_heap) + 1  # Remove most frequent task and decrement its count
                if count:  # If there are remaining tasks, add to the cooldown queue
                    queue.append((time + n, count))
                    
            if queue and queue[0][0] == time:  # Check if a task is ready to be scheduled again
                heapq.heappush(max_heap, queue.popleft()[1])
        
        return time