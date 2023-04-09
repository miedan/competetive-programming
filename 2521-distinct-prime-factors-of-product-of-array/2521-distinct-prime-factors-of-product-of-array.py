class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        
        dic = defaultdict(int)
        
        for product in nums:
            d = 2
            while d * d <= product:
                while product % d == 0:
                    product //= d
                    dic[d] += 1
                d += 1
        
            if product > 1:
                dic[product] += 1
                        
        return len(dic)
        
        