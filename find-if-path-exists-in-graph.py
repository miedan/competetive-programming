class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        graph = defaultdict(list)
        parent = {i : i  for i in range(n)}
       
        visited = set()
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        def dfs(node, par):

            if node in visited:
                return
            visited.add(node)

            for j in graph[node]:
                parent[j] = par
                dfs(j, par)
          

        for i in range(n):
            if i not in visited:
                dfs(i, i)

        if parent[source] == parent[destination]:
            return True
        else:
            return False