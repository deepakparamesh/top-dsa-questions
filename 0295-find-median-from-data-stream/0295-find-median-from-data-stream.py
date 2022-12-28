class MedianFinder:
        def __init__(self):
       
        # two heaps, large, small, minheap, maxheap
        # heaps should be equal size
            self.small, self.large = [], []  # maxHeap, minHeap (python default)

        def addNum(self, num: int) -> None:
            
            # cond 1: All the values in the small should be smaller or equal than the large heap
            if self.large and num > self.large[0]:
                heapq.heappush(self.large, num)
            else:
                heapq.heappush(self.small, -1 * num)
            
            # Cond2: len(small) should be appox. equal to len(large) 
            if len(self.small) > len(self.large) + 1:
                val = -1 * heapq.heappop(self.small)
                heapq.heappush(self.large, val)
            if len(self.large) > len(self.small) + 1:
                val = heapq.heappop(self.large)
                heapq.heappush(self.small, -1*val)
                
                
            

        def findMedian(self) -> float:
            if len(self.small) > len(self.large):
                return -1 * self.small[0]
            elif len(self.large) > len(self.small):
                return self.large[0]
            
            return (-1 * self.small[0] + self.large[0]) / 2 