class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}
        n = len(cost)

        def dp(idx):

            if idx >= n:
                return 0
            if idx not in memo:
                memo[idx] = cost[idx] + min(dp(idx+1),dp(idx+2))
            return memo[idx]

        return min((dp(0),dp(1)))