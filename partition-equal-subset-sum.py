class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        total = sum(nums)
        

        if total % 2 != 0:
            return False
        
        
        #total//2 = total // 2

        # @cache
        memo = {}

        def dp(i, cur_sum):

            if i >= len(nums):
                return False
                
            if (i, cur_sum) in memo:
                return memo[(i, cur_sum)]

            if cur_sum ==total//2:
                return True

            if cur_sum >total//2:
                return False
           
            pick = dp(i+1, cur_sum + nums[i])
            dont_pick = False
            if not pick:
                dont_pick = dp(i+1, cur_sum)
     

            

            memo[(i, cur_sum)] = pick or dont_pick
            return memo[(i, cur_sum)]

        return dp(0, 0)