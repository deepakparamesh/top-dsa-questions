class Solution:
    def maxArea(self, height: List[int]) -> int:
        result = 0
        left, right = 0, len(height) - 1
        maxHeight = max(height)
        
        while left < right:
          area = (right - left) * min(height[left], height[right])
          result = max(area, result)
          
          if height[left] < height[right]:
            left += 1
          else:
            right -=1
          
          if (right - left) * maxHeight <= result:
            break
          
        return result