class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:

        rank = [[0 for _ in range(n)] for _ in range(n) ]
        
        for i in range(len(preferences)):
            for j in range(len(preferences[i])):
                friend = preferences[i][j]
                rank[i][friend] = j
        
        ans = set()
        for i in range(len(pairs)-1):
            for j in range(i+1, len(pairs)):

                x, y, u, v = pairs[i][0], pairs[i][1], pairs[j][0], pairs[j][1]

                if rank[x][u] < rank[x][y] and rank[u][x] < rank[u][v]:
                    ans.add(x)
                    ans.add(u)

                if rank[x][v] < rank[x][y] and rank[v][x] < rank[v][u]:
                    ans.add(x)
                    ans.add(v)

                if rank[y][u] < rank[y][x] and rank[u][y] < rank[u][v]:
                    ans.add(y)
                    ans.add(u)

                if rank[y][v] < rank[y][x] and rank[v][y] < rank[v][u]:
                    ans.add(y)
                    ans.add(v)
                    
        return len(ans)