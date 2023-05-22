class Solution:
    def removeStones(self, edges: List[List[int]]) -> int:
        
        n = len(edges)
        roots = {i : i for i in range(n)}
        d = defaultdict(int)
        

        def find(x):
           if roots[x] != x:
               roots[x] = find(roots[x])
           return roots[x]
        
       
        def union(v1, v2):

            rootv1 = find(v1)
            rootv2 = find(v2)

            
            roots[rootv2] = rootv1
                
             

        for i in range(n):
            for j in range(i+1,):

                if edges[i][0] == edges[j][0] or edges[i][1] == edges[j][1]:
                    union(i, j)

        for i in roots:
            roots[i] = find(i)
            d[roots[i]] += 1
        
        return n - len(d)