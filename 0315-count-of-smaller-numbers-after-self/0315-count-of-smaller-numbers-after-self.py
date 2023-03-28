class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        self.count = [0]*len(nums)
        self.tmp = []
        for i in range(len(nums)):
            self.tmp.append([nums[i], i])
        self.merge(self.tmp, 0, len(self.tmp)-1)
        return self.count
        
        
    def merge(self, arr, left, right):
        if left == right:
            return [arr[left]]
        mid = left + (right - left) // 2
        lefthalf = self.merge(arr, left, mid)
        righthalf = self.merge(arr, mid+1, right)
        l = 0
        for k in range(len(lefthalf)):
            while l < len(righthalf)  and lefthalf[k][0] > righthalf[l][0]:
                l += 1
            self.count[lefthalf[k][1]] += l
            
        
        i , j = 0,0 
        
        temp = []
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i][0] < righthalf[j][0]:
                temp.append(lefthalf[i])
                i += 1
            else:
                
                temp.append(righthalf[j])
                j += 1
               
        while i < len(lefthalf):
            temp.append(lefthalf[i])
            i += 1
        while j < len(righthalf):
            temp.append(righthalf[j])
            j += 1
        return temp
        
                
        
        
        
            
        
    
        