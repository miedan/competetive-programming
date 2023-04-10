class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = {"}":"{", "]":"[", ")":"("}
        for char in s:
            if char in dic.values():
                stack.append(char)
            elif stack and dic[char] == stack [-1]:
                stack.pop()
            else:
                return False
        return stack == []