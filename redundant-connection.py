class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

         p = [i for i in range(len(edges)+ 1)]
         
         answer = []

         def find(x):

             cur = x
             while p[cur] != cur:
                 cur = p[cur]
             return cur
        
         def union(v1, v2):

             pv1 = find(v1)
             pv2 = find(v2)

             if pv1 == pv2:
                 answer.append([v1, v2])

             p[pv1] = p[pv2]
                

 
         for a, b in edges:
             union(a, b)

         return answer[-1]