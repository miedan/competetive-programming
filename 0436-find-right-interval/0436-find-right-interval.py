class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        dic = defaultdict(int)
        start = []
        for i in range (len(intervals)):
            dic[intervals[i][0]] = i
            start.append(intervals[i][0])
        start.sort()
        output = []
        for j in range(len(intervals)):
            right = bisect_left(start, intervals[j][1])
            if right >= len(start):
                output.append(-1)
            
            else:
                output.append(dic[start[right]])
        return output
            
            
        
        
       
     
       

            
       
    
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
                                