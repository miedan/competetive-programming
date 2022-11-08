class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        maximumheap =[-int(i) for i in nums]
        heapq.heapify(maximumheap)
        
        while k>1:
            heapq.heappop(maximumheap)
            k-=1
            
        return str(-maximumheap[0])
        