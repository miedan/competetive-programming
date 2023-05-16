class Solution:
    def checkIfPrerequisite(self, numcourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:

        que = deque([]) 
        output = [set() for i in range(numcourses)] 
        answer = []
        incoming = [0] * numcourses 
        graph  = defaultdict(list) 
        for a, b in prerequisites: 
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

        for a, b in queries:
            if a in output[b]:
                answer.append(True)
            else:
                answer.append(False)

                    
        return answer