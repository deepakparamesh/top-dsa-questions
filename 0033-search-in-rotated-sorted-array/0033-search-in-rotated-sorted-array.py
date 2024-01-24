class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        left = 0
        right = len(nums)-1
        
        while left <= right:
            middle = left + ((right - left) // 2)
            
            if nums[middle] == target:
                return middle
            
            # left sorted portion
            if nums[middle] >= nums[left]:
                if target > nums[middle] or target < nums[left]:
                    left = middle + 1
                else :
                    right = middle - 1
            # right sorted portion
            else:
                if target < nums[middle] or target > nums[right]:
                    right = middle - 1
                else:
                    left = middle +1
        
        return -1
    