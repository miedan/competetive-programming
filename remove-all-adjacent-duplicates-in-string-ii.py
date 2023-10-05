class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:

        stack  = [[s[0],1]]
        
        for j in range(1, len(s)) :

            i = s[j]
            if  stack and i == stack[-1][0] :
                stack[-1][1] += 1

                if stack[-1][1] == k:
                    stack.pop()

            else:
                stack.append([i,1])
            
                
        ans = ""
        for a, b in stack:
            ans += b * a
        return ans