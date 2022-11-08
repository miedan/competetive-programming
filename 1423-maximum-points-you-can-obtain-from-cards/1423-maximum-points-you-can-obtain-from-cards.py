class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        total = sum(cardPoints)
        
        m = n - k
        subarray_sum = sum(cardPoints[:m])
        
        min_sum = subarray_sum
        for i in range(m, n):
            subarray_sum += cardPoints[i]
            subarray_sum -= cardPoints[i - m]
            min_sum = min(min_sum, subarray_sum)
        return total - min_sum
        
        