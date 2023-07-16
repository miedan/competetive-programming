class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        memo = {}

        def dp(i, isbuying):

            if i >= len(prices):
                return 0

            if (i, isbuying) in memo:
                return memo[(i, isbuying)]

            cooldown = dp(i+1, isbuying)

            if isbuying:

                buy = dp(i+1, not isbuying) - prices[i]
                memo[(i, isbuying)] = max(buy, cooldown)

            else:
                sell = dp(i+2, not isbuying) + prices[i]
                memo[(i, isbuying)] = max(sell, cooldown)

            return memo[(i, isbuying)]
        return dp(0, True)