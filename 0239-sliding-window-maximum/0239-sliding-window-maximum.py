class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        que = collections.deque()
        arr = []
        for i in range(k):
            while que and nums[que[-1]] < nums[i]:
                que.pop()
            que.append(i)
        arr.append(nums[que[0]])
        
        for i in range(1, len(nums) - k + 1):
            while que and nums[que[-1]] < nums[i + k -1]:
                que.pop()
            if que and que[0] < i:
                que.popleft()
            que.append(i + k -1)
            arr.append(nums[que[0]])
        return arr
            
            
        