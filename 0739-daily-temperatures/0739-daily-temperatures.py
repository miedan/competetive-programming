class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = [] 
        
        for idx , tmp in enumerate(temperatures):
            while stack and tmp > stack[-1][0]:
                stacktmp , stackidx = stack.pop()
                ans[stackidx] = (idx - stackidx)
            stack.append([tmp, idx])
        return ans 
        
        