class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:

        dp = [[0 for _ in range(query_row + 1)] for _ in range(query_row + 1 )]
        dp[0][0] = poured

        for row in range(query_row):
            for col in range(len(dp[row])):
                temp =( dp[row][col]-1) / 2
                if temp > 0:
                    dp[row+1][col] += temp
                    dp[row+1][col+1] += temp
        return dp[query_row][query_glass] if dp[query_row][query_glass] <= 1 else 1