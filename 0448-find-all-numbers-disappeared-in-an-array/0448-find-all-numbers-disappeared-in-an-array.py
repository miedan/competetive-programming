class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        i = 0
        while i < len(nums):
            temp = nums[i]
            if temp != i +1 and temp != nums[temp - 1] and temp - 1 < len(nums):
                nums[i] , nums[temp-1] =  nums[temp - 1], nums[i]
            else:
                i += 1
        result = []
        for i in range(len(nums)):
            if nums[i] != i + 1:
                result.append(i + 1)
        return result

        
       