class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles = sorted(piles, reverse=True)
        sum = 0
        index = 1
        while index < len(piles):
            sum += piles[index]
            piles.pop()
            index += 2
        return sum
        