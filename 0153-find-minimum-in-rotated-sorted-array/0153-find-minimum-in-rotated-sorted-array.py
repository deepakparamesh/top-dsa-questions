class Solution:
    def findMin(self, nums: List[int]) -> int:
        result = float("inf")
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            middle = (left + right) // 2
            result = min(result, nums[middle])
            
            # we are in left sorted portion, minimum is found in the right
            if nums[middle] >= nums[right]:
                left = middle + 1
                
            # we are in right sorted portion, minimum is found in the left
            else :
                right = middle - 1
            
        return result