class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def backtrack(i, temp):
            if len(temp) == k:
                res.append(temp.copy())
                return
            for j in range(i, n+1):
                temp.append(j)
                backtrack(j+1, temp)
                temp.pop()
                
        backtrack(1, [])  
        return res
        
