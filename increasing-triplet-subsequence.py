class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:

        minimum = float('inf')
        maximum = float('inf')

        for i in range(len(nums)):
            
            if nums[i] <= minimum:
                minimum = nums[i]
            elif nums[i] <= maximum:
                maximum = nums[i]
            else :
                return True
        return False