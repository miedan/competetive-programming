class Solution:
    def numDecodings(self, s: str) -> int:

        n = len(s)
        memo = {n:1}
        
        def dp(i):
            
            if i in memo:
                return memo[i]
            
            if s[i] == "0":
                return 0

            total = dp(i+1)

            if ((i+1 < n) and ( s[i] == '1' or s[i] == '2' and s[i+1] in "0123456")):
                total += dp(i+2)
            memo[i] = total

            return memo[i]
        return dp(0)