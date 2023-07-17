class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:

        @cache
        def dp(total):
            
            if total > target:
                return 0

            if total == target:
                return 1
            
            ans = 0
            
            for num in nums:
                
                ans +=  dp(total + num)
                
            return ans

        return dp(0)