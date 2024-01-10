class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        result = right
        
        while left <= right:
            
            middle = (left + right) // 2
            
            totalHours = 0
            for pile in piles:
                totalHours += math.ceil(float(pile) / middle)
            
            if totalHours <= h:
                result = middle
                right = middle - 1
            else:
                left = middle + 1
        
        return result
            