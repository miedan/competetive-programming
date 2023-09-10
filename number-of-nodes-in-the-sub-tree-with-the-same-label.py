class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        
        graph = defaultdict(list)

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        self.ans = [0 for i in range(n)]

        def dfs(node, prev):

            count = Counter()
            count[labels[node]]=1
            
            for neigh in graph[node]:
                if neigh == prev:
                    continue
                count += dfs(neigh, node)
                                    
            self.ans[node] = count[labels[node]]
            return count
        
        dfs(0, None)
        return self.ans