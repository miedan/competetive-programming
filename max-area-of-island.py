class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        def dfs(grid, row, col):

            if not grid:
                return 0

            if  row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] == 0:
                return 0

            grid [row][col] = 0
            return 1 + dfs(grid, row + 1, col) + dfs(grid, row - 1, col)  + dfs(grid, row, col + 1) + dfs(grid, row, col - 1) 
            
        maxarea = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 :
                    
                    maxarea = max(maxarea, dfs(grid, i, j))

        return maxarea