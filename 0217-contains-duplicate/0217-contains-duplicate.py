class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        containsSet = set()
        
        for i in nums:
          if i in containsSet:
            return True
          containsSet.add(i)
        return False