class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for c in range(len(s)):
            if s[c] != "]":
                stack.append(s[c])
            else:
                substr = ""
                while stack[-1] != "[":
                    substr = stack.pop() + substr
                stack.pop()
                
                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                stack.append(int(k) * substr)
        return "".join(stack)
        