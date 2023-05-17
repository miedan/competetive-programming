class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        parent = {i : i for i in range(n)}

        def find(a):

            while parent[a] != a:
                a = parent[a]
            return a

        def union(v1, v2):

             parentv1 = find(v1)
             parentv2 = find(v2)
             parent[parentv1] = parent[parentv2]

        for a, b in edges:
            union(a, b)

        return find(source) == find(destination)