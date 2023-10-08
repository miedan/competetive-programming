class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:

        houses.sort()
        heaters.sort()

        n = len(heaters) - 1
        left, right = 0, 0
        radius = 0

        for house in houses:
            while right < n and house > heaters[right]:
                left, right = right, right + 1
                
            d1, d2 = abs(heaters[left] - house), abs(heaters[right] - house)
            
            radius = max(radius, min(d1, d2))
            
        
        return radius