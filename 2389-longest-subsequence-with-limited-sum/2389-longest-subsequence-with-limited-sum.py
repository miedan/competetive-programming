class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        res = [0]*len(queries)
        for i in range(len(queries)):
            target = queries[i] 
            sums = 0
            count = 0
            for num in nums:
                sums += num
                if sums <= target: 
                    count +=1
                    res[i] = count
                    
                else:
                    break
                
        return res
        