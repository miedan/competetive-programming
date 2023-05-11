class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:

        n = len(graph)
        color = [0] * n
        ans = []

        def safenode(node):

            if color[node] == 1:
                return False
            
            
            color[node] = 1

            for neigh in graph[node]:
                if color[neigh] == 2:
                    continue

                if safenode(neigh) == False:
                    return False

            color[node] = 2
            ans.append(node)
            return True


        for i in range(n):

            if color[i] == 0:

                safenode(i)
      
        return sorted(list(set(ans)))