class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        res = []
        for i in range(len(gain)):
            if i==0:
                res.append(0)
                res.append(gain[i])
            else:
                res.append(gain[i] + res[-1])
        return max(res)
        
        
        