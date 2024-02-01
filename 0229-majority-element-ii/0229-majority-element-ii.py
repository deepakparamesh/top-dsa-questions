class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
#         {
#             "3" :"2",
#             "2": "1"
#         } 
        
        
#         3/3 = 1
        
#         result = ['3']
        
#         Time : O(n) + O(n) => O(n)
#         space : O(n)
        
        majoritySize = len(nums) // 3
        hashMap = {}
        result = set()

        for num in nums:
            hashMap[num] = hashMap.get(num, 0) + 1
            if hashMap[num] > majoritySize:
                result.add(num)
        
        result = list(result)
        return result
        