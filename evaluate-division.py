class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:


        graph = defaultdict(list)
        for i, val in enumerate(equations):

            a, b = val
            graph[a].append((b, values[i]))
            graph[b].append((a, 1/values[i]))
                        
        def dfs(src, dest, visited):

            if src not in graph or dest not in graph:
                return -1.0

            if src == dest:
                return 1.0

            visited.add(src)

            for neigh, dist in graph[src]:
                # print(neigh)
                if neigh not in visited:
                    result = dfs(neigh, dest, visited)
                    
                    if result != -1.0:
                        
                        return dist * result
                    

            return -1.0

        ans = []
        for s, d in queries:
           
            ans.append(dfs(s, d, set()))

        return ans