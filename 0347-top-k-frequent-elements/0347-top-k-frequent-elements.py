class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_dict = {}
        
        for num in nums:
            if num not in num_dict:
                num_dict[num] = 1
            else:
                num_dict[num] += 1
        
        
        heap = []
        for key,val in num_dict.items():
            heap.append((-val, key))
        
        heapq.heapify(heap)
        res = []
        
        for _ in range(k):
            _,ans = heapq.heappop(heap)
            res.append(ans)
        return res
        