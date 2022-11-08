class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for n in num:
            while k>0 and stack and stack[-1]>n:
                k -= 1
                stack.pop()
            stack.append(n)
        stack = stack[:len(stack) - k]
        ans = "".join(stack)
        
        return str(int(ans)) if ans else "0"
        
        