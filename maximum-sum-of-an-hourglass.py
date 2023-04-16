class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:

        m = len(grid)
        n = len(grid[0])
        maxi = 0
        for i in range(1, m - 1):
            for j in range(1, n - 1):
                summ = grid[i][j] + grid[i- 1][j] + grid[i - 1][j + 1] + grid[i - 1][j - 1] + grid[i+ 1][j - 1] + grid[i + 1][j] + grid[i + 1][j + 1]
                maxi = max(maxi, summ)


        return maxi