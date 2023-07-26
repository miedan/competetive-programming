class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        memo = {}  

        def helper(i, buy):
            if i == n:
                return 0

            if (i, buy) in memo:
                return memo[(i, buy)]

            ans = helper(i + 1, buy)
            if buy:
                ans = max(ans, helper(i + 1, False) - prices[i])
            else:
                ans = max(ans, helper(i + 1, True) + prices[i] - fee)

            
            memo[(i, buy)] = ans
            return ans

        return helper(0, True)