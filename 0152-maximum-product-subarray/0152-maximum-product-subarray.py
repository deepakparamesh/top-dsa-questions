class Solution:
    def maxProduct(self, arr: List[int]) -> int:
#         prefix, suffix = 1,1
        
#         size = len(nums)
#         result = float("-inf")
#         for index in range(size):
#             if prefix == 0:
#                 prefix = 1
#             if suffix == 0:
#                 suffix = 0
            
#             prefix *= nums[index]
#             suffix *= nums[size - index - 1]
            
#             result = max(result, max(prefix, suffix))
        
#         return result
        n = len(arr) # size of array.

        pre, suff = 1, 1
        ans = float('-inf')
        for i in range(n):
            if pre == 0:
                pre = 1
            if suff == 0:
                suff = 1
            pre *= arr[i]
            suff *= arr[n - i - 1]
            ans = max(ans, max(pre, suff))
        return ans
            