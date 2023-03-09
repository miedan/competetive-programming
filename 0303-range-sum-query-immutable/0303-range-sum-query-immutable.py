class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix_1 = []
        summ =0
        for  i in range(len(nums)):
            summ += nums[i]
            self.prefix_1.append(summ)
            
       

    def sumRange(self, left: int, right: int) -> int:
        if left > 0:
            ans = self.prefix_1[right] - self.prefix_1[left-1]
            
        else:
            ans = self.prefix_1[right] 
        return ans
            
            
        
        
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)