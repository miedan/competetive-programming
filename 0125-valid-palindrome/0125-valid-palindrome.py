class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp = []
        for i in range(len(s)):
            if s[i].isalnum():
                temp.append(s[i])
        left = 0
        right = len(temp) - 1
        while left < right:
            if temp[right].lower() == temp[left].lower():
                right -= 1
                left += 1
            else:
                return False
        return True
            
                
        
#         .
#             length =len(s)
#         l,r=0,len(s)-1
        
#         while l<r:
#             while not s[l].isalnum() and l<r:l+=1
#             while not s[r].isalnum()and l<r:r-=1
#             if s[r].lower()!=s[l].lower():
#                 return False
#             r-=1;l+=1
#         return True

        