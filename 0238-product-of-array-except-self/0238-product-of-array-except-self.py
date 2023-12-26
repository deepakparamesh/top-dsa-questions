class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        result = [1] * (len(nums))
        prefix = 1
        for index,num in enumerate(nums):
            result[index] = prefix
            prefix = prefix * num
        
        postfix = 1
        for index in range(len(nums)-1,-1,-1):
            result[index] = result[index] * postfix
            postfix = postfix * nums[index]
        
        return result