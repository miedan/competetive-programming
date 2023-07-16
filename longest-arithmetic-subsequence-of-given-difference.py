class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:

        n = len(arr)

        dp = {}
        max_subsequence = 1

        for i in range(n):

            if arr[i] - difference in dp:
                dp[arr[i]] = 1 + dp[arr[i]-difference]
            else:
                dp[arr[i]] = 1
            

        return max(dp.values())