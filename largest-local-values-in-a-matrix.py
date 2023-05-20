class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        maxlocal = [[0 for _ in range(n -2)] for _ in range(n - 2)]
        
        for i in range(n - 2):
            for j in range(n - 2):
                
                for x in range(i, i + 3):
                    for y in range(j, j + 3):
                        maxlocal[i][j] = max(maxlocal[i][j], grid[x][y])
                 
        return maxlocal