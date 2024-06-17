class MedianFinder:

    def __init__(self):
        # Max-heap for the lower half
        self.max_heap = []
        # Min-heap for the upper half
        self.min_heap = []

    def addNum(self, num: int) -> None:
        # Add to max-heap
        heapq.heappush(self.max_heap, -num)
        
        # Balance the heaps by ensuring the smallest element of min-heap is greater than or equal to the largest element of max-heap
        if self.max_heap and self.min_heap and (-self.max_heap[0] > self.min_heap[0]):
            val = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, val)
        
        # Balance sizes: either both heaps are equal or max-heap has one more element than min-heap
        if len(self.max_heap) > len(self.min_heap) + 1:
            val = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, val)
        if len(self.min_heap) > len(self.max_heap):
            val = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -val)
        
    def findMedian(self) -> float:
        if len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        return (-self.max_heap[0] + self.min_heap[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()