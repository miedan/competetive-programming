class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        current_sum = 0
        result = 0
        prefix_sum = {0:1}
        
        for num in nums:
            current_sum += num
            difference = current_sum - k
            result += prefix_sum.get(difference, 0)
            prefix_sum[current_sum] = 1 + prefix_sum.get(current_sum, 0)
        return result
        