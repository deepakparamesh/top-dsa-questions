class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        # Time Complexity : O(n*m)
#         result = [-1] * len(nums1)
        
#         nums1Index = {value:index for index, value in enumerate(nums1)}
        
#         for index in range(len(nums2)):
#             if nums2[index] in nums1Index:
#                 for index2 in range(index+1, len(nums2)):
#                     if nums2[index2] > nums2[index]:
#                         resultIndex = nums1Index[nums2[index]]
#                         result[resultIndex] = nums2[index2]
#                         break
        
#         return result
        
        
        result = [-1] * len(nums1)
        nums1Index = {value:index for index, value in enumerate(nums1)}
        
        stack = []
        
        for index in range(len(nums2)):
            current = nums2[index]
            
            while stack and current > stack[-1]:
                val = stack.pop()
                resultIndex = nums1Index[val]
                result[resultIndex] = current
            
            if current in nums1Index:
                stack.append(current)
        return result
        