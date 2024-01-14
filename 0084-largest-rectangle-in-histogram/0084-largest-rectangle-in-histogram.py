class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = [] # pair: [index, height]
        
        for index, height in enumerate(heights):
            start = index
            while stack and stack[-1][1] > height:
                stackIndex, stackHeight = stack.pop()
                maxArea = max(maxArea, stackHeight * (index - stackIndex))
                start = stackIndex
            stack.append((start, height))
        
        # for i, h in enumerate(heights):
        #     start = i
        #     while stack and stack[-1][1] > h:
        #         index, height = stack.pop()
        #         maxArea = max(maxArea, height * (i - index))
        #         start = index
        #     stack.append((start, h))
        
        # There will be few left over items in the stack, we need to calculate the area for them too and then recalculate the area with maxArea
        for index, height in stack:
            area = height * (len(heights) - index)
            maxArea = max(area, maxArea)
        
        return maxArea
