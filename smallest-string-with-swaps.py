class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
         n = len(s)
         parent = {i : i for i in range(n)}
         d1 = defaultdict(list)
         d2 = defaultdict(list)
         op = list(s)
         

         def find(x):

             if parent[x] != x:
                 parent[x] = find(parent[x])
             return parent[x]

         def union(x,y):
             
             parentx = find(x)
             parenty = find(y)

             parent[parentx] = parenty

         for a, b in pairs:
             union(a, b)
          

         for i in parent:
             parent[i] = find(i)
         

         for i in parent:

             d1[parent[i]].append(i)
             d2[parent[i]].append(s[i])

         
         for i in d2:

             
             a = sorted(d1[i])
             b = sorted(d2[i])
             

             for j in range(len(a)):
                 op[a[j]] = b[j]
            
         return "".join(op)