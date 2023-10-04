class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        graph = defaultdict(list)
     
        for s, d, t in times:
            graph[s].append((d,t))
        

        time = {i+1: float('inf') for i in range(n)}
       
        visited = set()
       
        time[k] = 0
        
        heap = [(time[k], k)]
        
        while heap:
            
            popped =  heapq.heappop(heap)
            print(popped)
            t,src = popped
            if src  in visited:
                continue
            visited.add(src)

            for neigh in graph[src]:
                dest, tme = neigh
                
                if time[dest] > time[src] + tme:
                    
                    time[dest] = time[src] + tme
                
                    heapq.heappush(heap,(time[dest],dest))
        
        if max(time.values()) == float('inf'):
            return -1
        else:
            return max(time.values())