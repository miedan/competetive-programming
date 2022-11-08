class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key= lambda i: i[0])
        output = [intervals[0]]
        
        for first, last in intervals[1:]:
            end = output[-1][-1]
            
            if first <= end:
                output[-1][1]= max(end, last)
            else:
                output.append([first, last])
        return output
                              
         
    
         
        