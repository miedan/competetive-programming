class Solution:
    def minStartValue(self, nums: List[int]) -> int:
      
         
         for i in range(len(nums)):
                if i > 0:
                    nums[i] = nums[i] + nums[i-1]
                mini = min(nums)
                start_value = 1
                if mini < 1:
                    start_value = abs(mini) + 1
         return start_value                
            
        
        