class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        start = 0
        average = 0
        count = 0
        result = []
        total = 0 
        
        for end in range(len(arr)):
            total += arr[end]
            if((end)>= k-1):
                average = total//k
                result.append(average)
                total -= arr[start]
                start += 1
        for i in range (len(result)):
            if(result[i]>= threshold):
                count+=1
        return count
                
        