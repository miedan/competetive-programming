class Solution:
    def countPrimes(self, n: int) -> int:
        p = [True for i in range(n + 1)]
        d = 2
        while d * d <= n:
            if p[d] == True:
                for i in range(d * d, n+1, d):
                    p[i] = False
            d += 1
            
        count = 0
        for d in range(2, n+1):
            if p[d] and d < n:
                count += 1
            
        return count