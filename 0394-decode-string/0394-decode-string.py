class Solution:
    def decodeString(self, s: str) -> str:
        i = 0
        def helper():
            nonlocal i
            result = ""
            d = 0
            while i < len(s) and s[i] != ']':
                if s[i].isdigit():
                    d = d * 10 + int(s[i])
                elif s[i] == '[':
                    i += 1
                    temp = helper()
                    result += d * temp
                    d = 0
                else:
                    result += s[i]
                i += 1
            return result
        return helper()
            