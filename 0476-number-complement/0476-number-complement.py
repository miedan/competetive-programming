class Solution:
    def findComplement(self, num: int) -> int:
        c = [2 ** i for i in range(64)]
        s = 0
        i = 0
        while s < num:
            s += c[i]
            i += 1
        return (s ^ num)
       


        
        
        
        
        