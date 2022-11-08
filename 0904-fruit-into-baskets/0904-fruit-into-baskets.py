class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        right = 0
        left = 0
        max_fruit = 0 
        d = {}
        
        while right < len(fruits):
            d[fruits[right]] = right
            if len(d) >= 3:
                min_value = min(d.values())
                del d[fruits[min_value]]
                left = min_value +1
            max_fruit = max(max_fruit, right - left + 1)
            right += 1
        return max_fruit
        