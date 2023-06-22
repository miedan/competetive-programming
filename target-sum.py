class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        n = len(nums)
        @cache

        def dp(idx, total):

            if idx >= n:
                return 1 if total == target else 0

            return dp(idx + 1, total+ nums[idx]) + dp(idx + 1, total - nums[idx])
        return dp(0, 0)