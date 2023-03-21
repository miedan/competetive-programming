class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        d = defaultdict(int)
        end = []
        start = []
        for i in range (len(intervals)):
            d[intervals[i][0]] = i
            end.append(intervals[i][1])
            start.append(intervals[i][0])
        starts = sorted(list(d.keys()))
        temp = []
        for start, end in intervals:
            if end in d:
                temp.append(d[end])
            else:
                index = bisect.bisect_right(starts, end)
                if index >= len(starts):
                    temp.append(-1)
                else:
                    right = starts[index]
                    temp.append(d[right])
        return temp

            
        
        
     
       

            
       
    
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
                                