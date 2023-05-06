class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        for i in range(len(piles)):
            piles[i] = -(piles[i])
        heapify(piles)
        while k :
            now = heappop(piles)
            heappush(piles, now // 2)
            
            k -= 1
        summ = 0
        for i in range(len(piles)):
            summ += piles[i]
        return -(summ)