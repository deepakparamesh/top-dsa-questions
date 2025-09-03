class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def binarySearch(nums, target, findFirst):
            left, right = 0, len(nums) - 1
            result = -1
            
            while left <= right:
                mid = left + (right - left) // 2
                
                if nums[mid] == target:
                    result = mid
                    if findFirst:
                        right = mid - 1  # Search left for first occurrence
                    else:
                        left = mid + 1   # Search right for last occurrence
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            
            return result
        
        if not nums:
            return [-1, -1]
        
        first = binarySearch(nums, target, True)
        if first == -1:
            return [-1, -1]
        
        last = binarySearch(nums, target, False)
        return [first, last]