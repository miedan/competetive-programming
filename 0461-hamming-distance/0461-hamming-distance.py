class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        count = 0
        while max(x,y) != 0:
            if x %2 != y%2:
                count += 1
            x >>= 1
            y >>= 1
        return count
        
        
        