class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        dp = [inf  for i in range(amount + 1)]
        dp[0] = 0
        for i in range(amount + 1):
            for x in coins:
                if i - x >= 0:
                    dp[i] = min(dp[i - x] + 1, dp[i])          
        return dp[-1] if dp[-1] != inf else -1