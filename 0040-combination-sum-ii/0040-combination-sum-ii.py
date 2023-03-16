class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        

        def backtracking(i, curr, total):
            if total==target:
                res.append(curr[:])
                return
            if i>=len(candidates) or total>target:
                return

            curr.append(candidates[i])
            backtracking(i+1, curr, total+candidates[i])
            curr.pop()

            while i+1 < len(candidates) and candidates[i]==candidates[i+1]:
                i+=1
            backtracking(i+1, curr, total)
        candidates.sort()
        backtracking(0, [], 0)
        return res 






            
        
            
        