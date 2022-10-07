class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        cnt = 0
        res = 0
        for i in range(len(s)):
            if i > 0 and s[i] == s[i - 1]:
                cnt += 1
                summ += cost[i]
                maximum = max(maximum, cost[i])
            else:
                if cnt > 1:
                    res += summ - maximum
                cnt = 1
                summ = cost[i]
                maximum = cost[i]
        if cnt > 1:
            res += summ - maximum
        return res