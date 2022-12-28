class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        minHeap = []
        
        for x, y in points:
            distance = (x ** 2) + (y ** 2)
            minHeap.append([distance, x, y])
        
        heapq.heapify(minHeap)
        result = []
        
        for i in range (k):
            minValue = heapq.heappop(minHeap)
            result.append([minValue[1], minValue[2]])
        
        return result