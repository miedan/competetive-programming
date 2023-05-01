class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:

        n, m = len(mat), len(mat[0])

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        
        output = [[float('inf') for i in range(m)] for j in range(n)]
        que = deque()
        visited = set()
        
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    que.append((i, j))
                    visited.add((i, j))
                    output[i][j] = 0
        
        while que:
            row, col = que.popleft()
            for r, c in directions:
                if row + r >= 0 and col + c >= 0 and row + r < n and col + c < m and (row + r, col + c) not in visited:
                    output[row + r][col + c] = min(output[row + r][col + c], output[row][col] + 1)
                    que.append((row + r, col + c))
                    visited.add((row + r, col + c))
        
        return output