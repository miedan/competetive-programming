class Solution:
    def findComplement(self, num: int) -> int:
        s = [2 ** i for i in range(64)]
        summ = 0
        i = 0
        while summ < num:
            summ += s[i]
            i += 1
        return (summ ^ num)
            
        
        