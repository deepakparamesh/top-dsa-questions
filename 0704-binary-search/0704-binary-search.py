class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        
        while left <= right:
          mid = left + ((right - left) // 2) # This is where you made mistake you put (r-l)/2 -> as though process
          if nums[mid] == target:
            return mid
          elif (target < nums[mid]):
            right = mid - 1
          elif (target > nums[mid]):
            left = mid +1
        
        return -1