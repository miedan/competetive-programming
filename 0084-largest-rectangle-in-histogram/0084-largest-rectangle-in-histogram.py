class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        g_max = 0
        heights.append(-1)
        n = len(heights)
        for i in range(n):
            cur_leftbound = i 
            while stack  and stack[-1][0] > heights[i]:
                value , left_bound = stack.pop()
                cur_leftbound = left_bound
                g_max = max(g_max, value* (i - left_bound))
            stack.append((heights[i], cur_leftbound))
        return g_max
            
        
            
                
            
                
                
                
                
            
        
