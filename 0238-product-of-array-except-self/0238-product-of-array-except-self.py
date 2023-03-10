class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        current_value = 1
        n = len(nums)
        left = [1]
        
        for position in range(1, n):
            current_value *= nums[position - 1]
            left.append(current_value)

        current_value = 1
        right = [1]
        for position in range(n - 1, 0, -1):
            current_value *= nums[position]
            right.append(current_value)

        answers = []
        for i in range(n):
            answers.append(left[i] * right[n - i - 1])
        return answers
        


       