class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        maxReach = 0
    
        # Iterate over the array
        for i in range(len(nums)):
            # If the current index is beyond the maximum reach, return false
            if i > maxReach:
                return False
            # Update the maximum reach
            maxReach = max(maxReach, i + nums[i])

            # If the maximum reach is beyond or at the last index, return true
            if maxReach >= len(nums) - 1:
                return True

        # If the loop completes, return true
        return True