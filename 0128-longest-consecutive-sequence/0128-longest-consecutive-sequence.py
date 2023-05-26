class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        
        for num in nums:
          # To check if this is the beginning of a sequence
          if (num-1) not in numSet:
            currentLongest = 1
            while num+currentLongest in numSet: # This is where you made mistake, you put num+1
              currentLongest +=1
            
            longest = max(longest, currentLongest)
        
        return longest