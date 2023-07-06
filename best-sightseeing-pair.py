class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        n = len(values)
        dp = [0]*(n)

        dp[0] = values[0]
        value = 0
        
        for i in range(1, n):

            dp[i] = max(dp[i-1], values[i-1]+i-1)
            value = max(value, dp[i]+values[i]-i)
        
        return value