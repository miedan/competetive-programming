class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:       
   
        heap = []
        output = []
        heapify(heap)
    
        for i in range(min(len(nums1), k)):
            heappush(heap, (nums1[i]+nums2[0], nums1[i], nums2[0], 0))
        
        while k > 0 and heap:
            s, num1, num2, index = heappop(heap)
            output.append([num1, num2])

            if index + 1 < len(nums2):
                heappush(heap, (num1+nums2[index+1], num1, nums2[index+1], index+1))
            k -= 1
                
        return output