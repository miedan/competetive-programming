class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        res = []
        while n  :
            if n % 2 != 0:
                res.append(1)
                
            else:
                res.append(0)
            n >>= 1
        i = 0
        while i < len(res)-1:
            if res[i] == res[i + 1]:
                return False
            
            i += 1
        return True
    
        
    
            
        