class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        self.ans = []
        d  = defaultdict(list)
        for i in range (len(graph)):
            for num in graph[i]:
                d[i].append(num)
        
        #  {0: [1, 2], 1: [3], 2: [3]})
        def dfs(vertex, arr):
            
            if vertex == len(graph) - 1:
                arr.append(vertex)
                self.ans.append(arr[:])
                arr.pop()
                return 

            arr.append(vertex)
            
            for i in d[vertex]:
                dfs(i, arr)

            arr.pop()
        
        dfs(0, [])

        return self.ans