class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        maxArea = 0
        
        while left < right:
            currentArea = (right - left) * min(height[right], height[left])
            maxArea = max(currentArea, maxArea)
            
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        
        return maxArea

# Area of rectangle = (right - left) * Min(height[right], height[left])