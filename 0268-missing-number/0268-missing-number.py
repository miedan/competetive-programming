class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        arr = [-1] * (len(nums) + 1)
        for i in range(len(nums)):
            arr[nums[i]] = nums[i]
        for j in range(len(arr)):
            if arr[j] == -1:
                return j
        