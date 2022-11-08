class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        minmized_max_pair = 0 
        left_ptr = 0
        right_ptr = len(nums)-1
        
        while left_ptr < right_ptr:
            minmized_max_pair = max(minmized_max_pair,nums[left_ptr] + nums[right_ptr])
            left_ptr += 1
            right_ptr -= 1 
            
        return   minmized_max_pair
        
        