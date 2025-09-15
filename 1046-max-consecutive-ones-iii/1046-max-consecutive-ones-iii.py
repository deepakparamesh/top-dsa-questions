class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
        
        left = 0
        right = 0
        zeros_in_window = 0
        max_window_size = 0
        
        while right < len(nums):
            # Expand window by including nums[right]
            if nums[right] == 0:
                zeros_in_window += 1
            
            # Contract window while we have too many zeros
            while zeros_in_window > k:
                if nums[left] == 0:
                    zeros_in_window -= 1
                left += 1
            
            # Update answer with current valid window size
            current_window_size = right - left + 1
            max_window_size = max(max_window_size, current_window_size)
            
            # Move to next position
            right += 1
        
        return max_window_size

        