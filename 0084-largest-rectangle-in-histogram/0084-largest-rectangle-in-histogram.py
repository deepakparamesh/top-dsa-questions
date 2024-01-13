class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
#         maxArea = 0
#         stack = [] # [index, height]

#         for index, height in enumerate(heights):
#             start = index
#             while stack and stack[-1][1] > height :
#                 stackIndex, stackHeight = stack.pop()
#                 maxArea = max(maxArea, height * (index - stackIndex))
#                 start = stackIndex
#             stack.append((start, height))
        
#         for i, h in stack:
#             maxArea = max(maxArea, h * (len(heights) - i))
            
#         return maxArea
        maxArea = 0
        stack = []  # pair: (index, height)

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index
            stack.append((start, h))

        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        return maxArea