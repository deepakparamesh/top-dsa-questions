class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        # solution with extra space
#         majoritySize = len(nums) // 2
#         hashMap = {}
        
#         for num in nums:
            
#             hashMap[num] = hashMap.get(num, 0) + 1
            
#             if hashMap[num] > majoritySize:
#                 return num
        
        
        # Boyer-moore algorithm without extra space
        result, count = nums[0],0
        
        for num in nums:
            if count == 0:
                result = num
            if num == result: 
                count+=1
            else:
                count-=1
        
        return result