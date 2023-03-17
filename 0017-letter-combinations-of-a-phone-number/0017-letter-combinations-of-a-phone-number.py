class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone = {1 : '', 2 : 'abc', 3 : 'def', 4 : 'ghi', 5 : 'jkl', 6 : 'mno', 7 : 'pqrs', 8 : 'tuv', 9 : 'wxyz', 0 : ''}
        
        res = []
        def backtrack (i, combination):
            if len(combination) == len(digits):
                res.append(''.join(combination))
                return 
            d = phone[int(digits[i])]
            for j in range (len(d)):
                combination.append(d[j])
                backtrack( i+1, combination)
                combination.pop()
                
        if len(digits )== 0:
            return []
        
        backtrack(0, [])
        return res
        
        
        
        
        
        
        
        