class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        self.res = []
        n = len(nums)
        def backtrack(idx,arr):
            self.res.append(arr.copy())

            if idx >= n:
                return 

            for i in range(idx, n):
                arr.append(nums[i])
                backtrack(i + 1, arr)
                arr.pop()

        backtrack(0,[])
        return self.res