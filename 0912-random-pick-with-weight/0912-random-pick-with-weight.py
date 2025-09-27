class Solution:

    def __init__(self, w: List[int]):
        self.prefix_sums = []
        running_sum = 0

        for weight in w:
            running_sum += weight
            self.prefix_sums.append(running_sum)
        
        self.total_weight = running_sum
        

    def pickIndex(self) -> int:
        
        target = random.random() * self.total_weight

        left, right = 0, len(self.prefix_sums)

        while left < right:
            mid = (left + right) // 2
            if self.prefix_sums[mid] < target:
                left = mid + 1
            else:
                right = mid
        
        return left


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()