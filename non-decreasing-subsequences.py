class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        
        def backtrack(idx, arr):

            if len(arr) >= 2:
                self.res.append(arr.copy())
            
            used = set()
            for i in range(idx, len(nums)):
                if nums[i] in used:
                    continue
                
                if not arr or nums[i] >= arr[-1]:
                    used.add(nums[i])
                    arr.append(nums[i])
                    backtrack(i + 1, arr)
                    arr.pop()
        
        backtrack(0, [])
        return self.res