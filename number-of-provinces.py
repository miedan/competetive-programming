class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
         # adj matrix to adg list
        adjlist = defaultdict(list)
        for i in range(len(isConnected)):
            for j in range(len(isConnected[i])):
                if isConnected[i][j] == 1:
                    adjlist[i + 1].append(j +1)
        # print (adjlist)
        visited = set()
        def dfs(vertex):
            
            
            if vertex in visited:
                return 
                
            visited.add(vertex)
            for i in adjlist[vertex]:
                if i not in visited:
                    dfs(i)

        province = 0
        for i in range(1, len(adjlist) + 1):
            if i not in visited:
                dfs(i)
                province += 1
        return province