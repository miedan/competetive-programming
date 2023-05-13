class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
       
        que = deque([]) 
        output = [set() for i in range(n)] 
        incoming = [0] * n 
        graph  = defaultdict(list) 
        for a, b in edges: 
            graph[a].append(b) 
            incoming[b] += 1 
       
 
        for index, count in enumerate(incoming): 
            if count == 0: 
                que.append(index) 
        
 
        while que: 
            now = que.popleft() 
            for i in graph[now]: 
                incoming[i] -= 1
                output[i].add(now)

                
                for j in output[now]:
                    output[i].add(j)

                if incoming[i] == 0: 
                    que.append(i) 

        for i in range(n):
            output[i] = sorted(list(output[i]))
                    
                    
        return output