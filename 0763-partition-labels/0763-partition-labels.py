class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        endindex = {}
        
        for idx , ch in enumerate(s):
            endindex[ch] = idx
            
        result = []
        end, size = 0, 0
        for idx , ch in enumerate(s):
            size += 1
            end = max(end, endindex[ch])
            
            if idx==end:
                result.append(size)
                size = 0
                
        return result
        