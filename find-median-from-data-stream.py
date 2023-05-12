class MedianFinder:

    def __init__(self):

        
        self.minheap = []
        self.maxheap = []
        heapify(self.minheap)
        heapify(self.maxheap)
        

    def addNum(self, num: int) -> None:

        if not self.minheap and not self.maxheap:
                heappush(self.minheap, num)

        
        elif len(self.minheap) - len(self.maxheap) >= 1 :
            if self.maxheap and num  <= -(self.maxheap[0]) : 
                heappush(self.maxheap, -(num))
            else:
                heappush(self.minheap, num)
                now = heappop(self.minheap)
                heappush(self.maxheap, -(now))
                
        elif (len(self.maxheap) - len(self.maxheap)) >= 1:
            if num <= -(self.heapmax[0]): 
                self.cur = heappop(self.heapmax)
                heappush(self.minheap, -(cur))
            else:
                heappush(self.minheap, num)

        else:

            
            if num > -(self.maxheap[0]):
                heappush(self.minheap, num)
            else:

                heappush(self.maxheap, -(num))
                temp = heappop(self.maxheap)
                heappush(self.minheap, -temp)


    def findMedian(self) -> float:

        if len(self.minheap) > len(self.maxheap):
            return (self.minheap[0])
        
        else:
            return (self.minheap[0] + (-(self.maxheap[0]))) / 2
            
        

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()