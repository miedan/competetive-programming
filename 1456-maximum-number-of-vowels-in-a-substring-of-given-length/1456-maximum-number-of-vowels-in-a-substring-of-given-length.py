class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        count = 0
        for i in range(k):
            if s[i] in vowels:
                count += 1
                
        l = 0
        r = k-1
        max_vowel_count = count
        while r<len(s) - 1:
            if s[l] in vowels:
                count -= 1
            
            l+=1
            r+=1
            if s[r] in vowels:
                count += 1
            max_vowel_count = max(max_vowel_count, count)
            
        return  max_vowel_count
        