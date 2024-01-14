class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = [] # pair: [index, height]
        
        for index, height in enumerate(heights):
            # The start index denotes from where the specific height starts, if the height starts from previous index.
            start = index
            while stack and stack[-1][1] > height:
                stackIndex, stackHeight = stack.pop()
                maxArea = max(maxArea, stackHeight * (index - stackIndex))
                start = stackIndex
            stack.append((start, height))
        
        # There will be few left over items in the stack, we need to calculate the area for them too and then recalculate the area with maxArea
        for index, height in stack:
            area = height * (len(heights) - index)
            maxArea = max(area, maxArea)
        
        return maxArea
