class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        n = len(nums)
        left = 0
        right = 1  

        while left < n and right < n:

            if nums[right] + nums[left] == target:
                return [left, right] 
            else:
                right += 1

            if right == n: 
                left += 1
                right = left + 1

        

        
