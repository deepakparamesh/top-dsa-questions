class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        
        # using extra memory.
#         majoritySize = len(nums) // 3
#         hashMap = {}
#         result = set()

#         for num in nums:
#             hashMap[num] = hashMap.get(num, 0) + 1
#             if hashMap[num] > majoritySize:
#                 result.add(num)
        
#         result = list(result)
#         return result
        
        # without using extra memory, boyre-moore algorithm
        count1, count2 = 0,0
        element1, element2 = float('-inf'),float('-inf')
        
        for num in nums:
            if count1==0 and num != element2:
                element1 = num
                count1 = 1
            elif count2==0 and num != element1:
                element2 = num
                count2 = 1
            elif num == element1:
                count1 += 1
            elif num == element2:
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1
        
        count1, count2 = 0,0
        for num in nums:
            if num == element1:
                count1+=1
            if num == element2:
                count2 += 1
        
        result = []
        majoritySize = len(nums) // 3
        if count1 > majoritySize:
            result.append(element1)
        if count2 > majoritySize:
            result.append(element2)
            
        return result
        
        
        
        
        
        