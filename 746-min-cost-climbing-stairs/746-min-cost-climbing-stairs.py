class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # I should have a function which determines the minimum step required for the given list of cost.
        # I should find the min between 2 subArrays 1. starting from 0 2. starting from 1
#         newCost = cost.append(0)
#         dp=[]
#         def helper(newCost):
#             dp[0] = newCost[0]
#             dp[1] = min(newCost[0], newCost[1])
#             for i in range(2,len(newCost)):
#                 dp[i] = min(dp[i-2] + newCost[i], dp[i-1])
                
#             return dp[len(newCost) - 1]
        
#         return min(helper(newCost), helper(newCost[1:]))
        for i in range(len(cost) - 3, -1, -1):
            cost[i] += min(cost[i + 1], cost[i + 2])

        return min(cost[0], cost[1])