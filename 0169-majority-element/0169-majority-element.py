class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        # solution with extra space
#         majoritySize = len(nums) // 2
#         hashMap = {}
        
#         for num in nums:
            
#             hashMap[num] = hashMap.get(num, 0) + 1
            
#             if hashMap[num] > majoritySize:
#                 return num
        
        
        # 3 Boyer-moore algorithm without extra space
        result, count = 0,0
        
        for num in nums:
            if count == 0:
                result = num
            count += (1 if num == result else -1)
        
        return result