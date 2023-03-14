class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [(0, -1)]
        g_max = 0
        heights.append(-1)
        n = len(heights)
        for i in range(1, n):
            cur_leftbound = i -1 
            while stack  and heights[stack[-1][0]] > heights[i]:
                ind , left_bound = stack.pop()
                cur_leftbound = left_bound
                g_max = max(g_max, heights[ind]* (i - left_bound -1))
            stack.append((i, cur_leftbound))
        return g_max
            
        
            
                
            
                
                
                
                
            
        
