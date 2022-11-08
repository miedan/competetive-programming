class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
       nums.sort()
       l = 0
       s = 0
       ans = 1
       for r in range(len(nums)):
           while (r-l)*nums[r] > (s+k)  and l<r:
               s-=nums[l]
               l+=1
           s+=nums[r]
           ans = max(ans,r-l+1)
       return ans