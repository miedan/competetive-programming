class Solution:
    def rob(self, nums: List[int]) -> int:

        n = len(nums)
        @cache
        
        def dfs(i, flag):

            if (i >= n or (i == n - 1 and flag)):
                return 0 

            return max(dfs(i + 1, flag), nums[i] + dfs(i + 2, flag))

        return max(dfs(1, False), nums[0] + dfs(2, True))