class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        n = len(triangle)
        @cache
        
        def dp(row, col):

            if row == n-1:
                return triangle[row][col]
                
            return triangle[row][col] + min(dp(row+1, col), dp(row+1, col+1))
            
        return dp(0, 0)