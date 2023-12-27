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
                maxLeft = max(height[left],maxLeft)
                left += 1
            elif maxRight < maxLeft:
                waterTrap = min(maxLeft, maxRight) - height[right]
                if(waterTrap > 0):
                    result += waterTrap
                maxRight = max(height[right], maxRight)
                right -= 1
        return result