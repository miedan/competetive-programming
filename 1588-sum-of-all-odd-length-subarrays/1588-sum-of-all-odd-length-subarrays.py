class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        
        ans = 0
        for i in range(len(arr)):
            sum = 0
            for j in range(i, len(arr)):
                sum += arr[j]
                if(i-j+1) % 2 != 0:
                    ans+= sum
        return ans 
            
        
        