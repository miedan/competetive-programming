class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        result = 0
        for idx in range(1, len(arr)-1):
            if arr[idx-1] < arr[idx]>arr[idx + 1]:
                l=r=idx
                
                while l>0 and arr[l] > arr[l-1]:
                    l -= 1
                    
                while r+1 <len(arr) and arr[r] > arr[r+1]:
                    r+=1
                    
                result = max(result, (r-l+1))
        return result
        
        