class Solution:
    def validMountainArray(self, nums: List[int]) -> bool:
        i = 0
        if len(nums) < 3:
            return False
         
        i,j=0,len(nums)-1
        while i<j and nums[i]<nums[i+1]:
            i+=1
        while j>0 and nums[j]<nums[j-1]:
            j-=1
        if i==j and j!=len(nums)-1 and i!=0:
            return True
        return False
        
                
        