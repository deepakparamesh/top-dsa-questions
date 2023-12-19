class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
#         newSet = set()
        
#         for num in nums:
#             if num not in newSet:
#                 newSet.add(num)
#             else:
#                 return True
        
#         return False
        
        newSet = set()
        
        for num in nums:
            if num in newSet:
                return True
            newSet.add(num)
        
        return False