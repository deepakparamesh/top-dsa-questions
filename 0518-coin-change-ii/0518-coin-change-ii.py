class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # Initialize DP array with zero and set dp[0] to 1
        dp = [0] * (amount + 1)
        dp[0] = 1

        # Fill the DP array
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]

        return dp[amount]