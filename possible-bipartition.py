class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:

        graph = defaultdict(list)
        color = defaultdict(int)

        for a,b in dislikes:
            graph[a].append(b)
            graph[b].append(a)
            color[a] = -1
            color[b] = -1
       
        def dfs(node):

            for neigh in graph[node]:
                if color[neigh] == -1:
                    color[neigh] = 1 - color[node]

                    if not dfs(neigh):
                        return False
                elif color[neigh] == color[node]:
                    return False
            return True
    

        for i in graph:
            if color[i] == -1:
                color[i] = 0
                if not dfs(i):
                    return False
        return True