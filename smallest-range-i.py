class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:

        if len(nums) == 1:
            return 0

        if max(nums) == min(nums):
            return 0
 
        if (max(nums)-k) - (min(nums)+k) < 0 :
            return 0 

        else:
            
            return (max(nums)-k) - (min(nums)+k)