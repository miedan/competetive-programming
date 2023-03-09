class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        dic = {}
        max_size = 0
        
        for right in range(len(s)):
            if s[right] in dic:
                dic[s[right]] += 1
            else:
                dic[s[right]] = 1
            while (right - left + 1) - max(dic.values()) > k:
                dic[s[left]] -= 1
                left +=1
            max_size = max(max_size, (right - left) + 1)
        return max_size
            
        
        