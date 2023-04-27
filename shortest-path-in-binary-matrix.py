class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0], [-1, 1], [1, -1], [1, 1], [-1, -1]]

        n= len(grid)
        
        que = deque([(0, 0, 1)])
        visited = set((0, 0))
        

        if grid[0][0] != 0 or grid[n - 1][n - 1] != 0:
                return -1

        

        while que:

            r, c, path = que.popleft()

            if r == n - 1 and c == n- 1:
                return path
            
            
            for i, j in directions:

                if r + i >= 0 and c + j >= 0 and r + i < n and c + j < n and grid[r + i][c + j] == 0 and (r + i, c + j) not in visited:

 
                    que.append((r + i, c + j, path + 1))
                    visited.add((r + i, c + j))
        return - 1