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

        
        # while pointer < n:
        #     curr = nums[pointer]
        #     if curr - 1 < n and curr - 1 != pointer and curr != nums[curr - 1]:
        #         nums[pointer], nums[curr - 1] = nums[curr - 1], nums[pointer]
        #     else:
        #         pointer += 1

        # # Find all missing numbers 
        # res = []
        # for i in range(n):
        #     if nums[i] != i + 1:
        #         res.append(i + 1)

        # return res