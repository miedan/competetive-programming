class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        dp = [[0 for i in range(n)] for j in range(m)]

        dp[0][0] = 1

        for row in range(m):
            for col in range(n):

                if row == 0 and col == 0:
                    continue

                dp[row][col] += dp[row -1][col] + dp[row][col-1] 

        return dp[-1][-1]