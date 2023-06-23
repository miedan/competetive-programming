class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:

        n = len(questions)

        memo = {}

        def dp(row):

            if row >= n:
                return 0

            if row not in memo:
                memo[row] = max(questions[row][0] + dp(row + questions[row][1] + 1), dp(row+1))
            
            return memo[row]

        return dp(0)