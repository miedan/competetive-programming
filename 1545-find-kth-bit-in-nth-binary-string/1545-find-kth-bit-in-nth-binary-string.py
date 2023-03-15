class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        arr = self.rec(n)
        return arr[k-1]
        
   
    def rec(self, n):
        if n == 1:
            return "0"
        temp = self.rec(n-1)
        str_inv = []
        
        for n in temp:
            if n == "0":
                str_inv.append("1")
            else:
                str_inv.append("0")
            
        str_inv.reverse()
        string1 = "".join(str_inv)
        return temp + "1" + string1
        
        