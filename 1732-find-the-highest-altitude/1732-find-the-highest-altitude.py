class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        # bruteforce
        # res = []
        #     if i==0:
        #         res.append(0)
        #         res.append(gain[i])
        #     else:
        #         res.append(gain[i] + res[-1])
        # return max(res)
        maxi = 0
        ans = 0
        for i in range(len(gain)):
            ans += gain[i]
            maxi = max(ans, maxi)
        return maxi
                
            
        
        
        
        