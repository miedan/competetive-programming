class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        
        graph = defaultdict(list)

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        self.ans = [0 for i in range(n)]

        def dfs(node, prev):

            count = Counter()
            label = labels[node]
            count[label]=1
            
            for nei in graph[node]:
                if nei == prev:
                    continue
                count += dfs(nei, node)
                                    
            self.ans[node] = count[label]
            return count
        
        dfs(0, None)
        return self.ans