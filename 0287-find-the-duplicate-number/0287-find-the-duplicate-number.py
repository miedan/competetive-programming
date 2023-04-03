class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums) :
            temp = nums[i]
            if temp != i + 1 and temp != nums[temp - 1] and temp - 1 < len(nums):
                nums[i], nums[temp - 1] = nums[temp-1], nums[i]
            else:
                i += 1
        return nums[-1]
    
    
   