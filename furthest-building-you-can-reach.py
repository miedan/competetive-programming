class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        gap = []
        heapify(gap)
        for i in range(len(heights) - 1):
            
            if heights[i + 1] > heights[i]:
                heappush(gap, heights[i + 1] - heights[i])

                if len(gap) > ladders:
                    bricks = bricks - heappop(gap)

                if bricks < 0:
                    return i
        
        return len(heights) - 1