class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
       
        res = []
        que = collections.deque()
        for i, num in enumerate(nums):
            while que and num >= nums[que[-1]]:
                que.pop()
            que.append(i)
            
            if i + 1 >= k:
                res.append(nums[que[0]])
            
            if i - que[0] + 1 == k:
                que.popleft()
        
        return res