class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0  # Left pointer of sliding window
        zeros_count = 0  # Count of zeros in current window
        max_length = 0  # Maximum valid window length found
        
        # Expand window with right pointer
        for right in range(len(nums)):
            # Add current element to window
            if nums[right] == 0:
                zeros_count += 1
            
            # Shrink window if we have too many zeros
            while zeros_count > k:
                if nums[left] == 0:
                    zeros_count -= 1
                left += 1
            
            # Update maximum length (current window is always valid here)
            current_length = right - left + 1
            max_length = max(max_length, current_length)
        
        return max_length

        