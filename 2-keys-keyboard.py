class Solution:
    def minSteps(self, n: int) -> int:

        if n == 1:
            return 0
       
        res = [] 

        d = 2  
        while d <= n:
            while n % d == 0:
                n /= d
                res.append(d)
            d += 1

        return sum(res)