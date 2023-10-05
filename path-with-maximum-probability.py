class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:

        graph = defaultdict(list)
        
     
        for i in range (len(edges)):

            s,d = edges[i]
            graph[s].append((d,succProb[i]))
            graph[d].append((s,succProb[i]))
            
     
        

        success = {i: float('inf') for i in range(n)}
       
        visited = set()
       
        success[start] = 1
        
        heap = [(-1, start)]
        
        while heap:
            
            popped =  heapq.heappop(heap)
            
            s,src = popped

            if src  in visited:
                continue
            visited.add(src)

    
            for neigh in graph[src]:
                
                dest, sucess = neigh
                
                if  dest not in visited:

                    if success[dest] > s * sucess:
                        
                        success[dest] = s * sucess
                    
                        heapq.heappush(heap,(success[dest],dest))
        
        if success[end] == float('inf'):
            return 0
        else:
            return -(success[end])