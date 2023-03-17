class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
       
        phone= {1 :'', 2:'abc', 3:'def', 4:'ghi', 5 :'jkl', 6:'mno', 7:'pqrs', 8:'tuv', 9 : 'wxyz', 0 : ''}
        
        res = []
        def backtrack(i,combination):
            
            if len(combination) == len(digits):
                res.append(''.join(combination))
                return
            vaule = phone[int(digits[i])]
            for j in range(len(vaule)):
                combination.append(vaule[j])
                backtrack(i+1,combination)
                combination.pop()
        if len(digits )== 0:
            return []
        if len(digits ) == 1:
            return phone[int(digits[0])]
        backtrack(0,[])
        
        
        
        return res
            
            
            
        
        
            
            
        
        
        
        
        