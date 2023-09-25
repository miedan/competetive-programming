class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:

        memo = {}
        n = len(scores)
        players = [(ages[i], scores[i]) for i in range(n)]
        players.sort()
        
        dp = [0 for i in range(n)]

        for i in range(n):
            dp[i] = players[i][1]
            
            for j in range(i):
                if players[j][1] <= players[i][1] or players[i][0] == players[j][0]:
                    dp[i] = max(dp[i], players[i][1] + dp[j])
                
        
        return max(dp)