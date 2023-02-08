class Solution:
    def maxDepth(self, s: str) -> int:
       
        current_max = 0
        max = 0
        n = len(s)
        for i in range(n):
            if s[i] == '(':
                current_max += 1
                if current_max > max:
                    max +=1
            if s[i] == ')':
                current_max -= 1
        return max
                
