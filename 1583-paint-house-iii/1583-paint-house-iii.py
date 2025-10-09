class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        
        INF = float('inf')
        dp = [[[INF]*(target + 1) for _ in range(n+1)]for _ in range(m)]

        if houses[0] == 0:
            for color in range(1,n+1):
                dp[0][color][1] = cost[0][color-1]
        else:
            dp[0][houses[0]][1] = 0
        
        for i in range(1,m):
            if houses[i]==0:

                for curr_color in range(1,n+1):
                    paint_cost = cost[i][curr_color-1]

                    for prev_color in range(1, n+1):
                        for neighborhoods in range(1, min(i+2, target+1)):
                            prev_cost=dp[i-1][prev_color][neighborhoods]

                            if prev_cost == INF:
                                continue
                            
                            if curr_color == prev_color:
                                new_neighborhoods = neighborhoods
                            else:
                                new_neighborhoods = neighborhoods + 1
                            
                            if new_neighborhoods <= target:
                                dp[i][curr_color][new_neighborhoods] = min(dp[i][curr_color][new_neighborhoods],prev_cost + paint_cost)
            else:
                curr_color= houses[i]

                for prev_color in range(1,n+1):
                    for neighborhoods in range(1, min(i+2, target+1)):
                        prev_cost = dp[i-1][prev_color][neighborhoods]

                        if prev_cost == INF:
                            continue
                        
                        if curr_color == prev_color:
                            new_neighborhoods = neighborhoods
                        else:
                            new_neighborhoods = neighborhoods + 1
                        
                        if new_neighborhoods <= target:
                            dp[i][curr_color][new_neighborhoods] = min(
                                dp[i][curr_color][new_neighborhoods],
                                prev_cost
                            )
        
        min_cost = INF
        for color in range(1,n+1):
            min_cost = min(min_cost, dp[m-1][color][target])
        
        return min_cost if min_cost != INF else -1





        # houses = [0,0,0,0,0] cost = [[1,10],[10,1],[10,1],[1,10],[5,1]]
        # m=5 colors, n=2, target=3

        # House 0: 1,2...n
                 
        # House 1: for each state from house0
        #         - same color as house 0 -> keep neighborhood count
        #         - different color -> increment neighborhood count

