class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        right = 0
        left = 0
        max_fruit = 0 
        dic = {}
        
        while right < len(fruits):
            dic[fruits[right]] = right
            if len(dic) >= 3:
                min_value = min(dic.values())
                del dic[fruits[min_value]]
                left = min_value +1
            max_fruit = max(max_fruit, right - left + 1)
            right += 1
        return max_fruit
        