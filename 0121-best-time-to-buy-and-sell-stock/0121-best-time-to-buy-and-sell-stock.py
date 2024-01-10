class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minValue = prices[0]
        
        for price in prices:
            if price < minValue:
                minValue = price
            profit = price - minValue 
            maxProfit = max(maxProfit, profit)
        
        return maxProfit
        
