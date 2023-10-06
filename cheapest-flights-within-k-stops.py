class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        graph = defaultdict(list)
     
        for s, d, t in flights:
            graph[s].append((d,t))
        

        distance = {i: float('inf') for i in range(n)}
       
        visited = set()
       
        distance[src] = 0
        
        heap = [(0,0,src)]
        
        while heap:
            
            popped =  heapq.heappop(heap)
            
            count, weight,node = popped

         
            for neigh in graph[node]:
                dest, w = neigh
                
                if distance[dest] > weight + w and count <= k:
                    
                    distance[dest] = weight + w
        

                    heapq.heappush(heap,(count +1, distance[dest],dest))

        if distance[dst] == float('inf'):
            return -1
        # print(distance)
        return distance[dst]