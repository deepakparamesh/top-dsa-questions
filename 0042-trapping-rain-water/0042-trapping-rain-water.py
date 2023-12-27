class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        maxLeft, maxRight = height[left], height[right]
        result = 0

        while left <= right:
            if maxLeft <= maxRight:
                waterTrap = min(maxLeft, maxRight) - height[left]
                if(waterTrap > 0):
                    result += waterTrap
                if height[left] > maxLeft:
                    maxLeft = height[left]
                left += 1
            elif maxRight < maxLeft:
                waterTrap = min(maxLeft, maxRight) - height[right]
                if(waterTrap > 0):
                    result += waterTrap
                if height[right] > maxRight:
                    maxRight = height[right]
                right -= 1
        return result