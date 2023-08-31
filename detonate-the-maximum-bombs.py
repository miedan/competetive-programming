class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        graph = defaultdict(list)

        for i in range(len(bombs)):
            for j in range(len(bombs)):
               if i != j:
                   if( bombs[i][0] - bombs[j][0]) ** 2 + (bombs[i][1] - bombs[j][1]) ** 2 <= (bombs[i][2]) **2:
                        graph[i].append(j)

        def dfs(node, visited):
            visited.add(node)
            for neigh in graph[node]:
                if neigh not in visited:
                    visited.add(neigh)
                    dfs(neigh,visited)
                
            return len(visited)


        ans = 0
        for i in range(len(bombs)):
            ans = max(ans,dfs(i,set([i])))
        return ans