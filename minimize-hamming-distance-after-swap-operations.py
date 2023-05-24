class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:

        parent = { i : i for i in range(len(source))}
        hamdist = 0
        d = defaultdict(lambda:defaultdict(int))

        def find(x):

            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):

            parentx = find(x)
            parenty = find(y)

            parent[parentx] = parenty

        for a, b in allowedSwaps:
            union(a,b)
                
        for i in range(len(source)):
            par = find(i)
            d[par][source[i]] += 1
        
        for i in range(len(target)):

            if d[parent[i]][target[i]] > 0:
                d[find(i)][target[i]] -= 1
                
            else:
                hamdist += 1
        return hamdist
            
# find(i)