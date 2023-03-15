class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        que = collections.deque()
        summ = 0
        que.append([0, 0])
        res = float('inf')
        
        for i, val in enumerate(nums):
            summ += val
            while que and summ - que[0][1] >= k:
                res = min(res, i - que[0][0] + 1 )
                que.popleft()
            while que and summ <= que[-1][1]:
                que.pop()
            que.append([i+1, summ])
        if res < float('inf'):
            return res
        return -1