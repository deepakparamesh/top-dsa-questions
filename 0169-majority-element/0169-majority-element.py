class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        majoritySize = len(nums) // 2
        hashMap = {}
        
        for num in nums:
            
            hashMap[num] = hashMap.get(num, 0) + 1
            
            if hashMap[num] > majoritySize:
                return num
        
        
        
        