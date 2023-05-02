class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:

        n, m = len(grid1), len(grid1[0])
        visited = set()


        def dfs(r, c):

            if r < 0 or c < 0 or r >= n or c >= m or (r, c) in visited or grid2[r][c] == 0:
                return True

            visited.add((r, c))
            is_subiland = True
            if grid1[r][c] == 0:
                is_subiland = False

            
            is_subiland &= dfs(r, c - 1)
            is_subiland &= dfs(r, c + 1)
            is_subiland &= dfs(r - 1, c)
            is_subiland &= dfs(r + 1, c)
            return is_subiland

        count = 0
        for r in range(n):
            for c in  range(m):
                if grid2[r][c] == 1 and (r, c) not in visited and dfs(r, c):
                    count += 1

        return count