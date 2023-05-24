class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        previousMap = {} # value -> index
        
        for i, n in enumerate(nums):
          difference = target - n
          if difference in previousMap:
            return [previousMap[difference], i]
          previousMap[n] = i