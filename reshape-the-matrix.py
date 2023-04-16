class Solution:
    def matrixReshape(self, matrix: List[List[int]], r: int, c: int) -> List[List[int]]:

        n = len(matrix)
        m = len(matrix[0])
        new = [[0] * c for _ in range (r)]

        if m * n  !=  r * c:
            return matrix

        x = 0
        for i in range(r):
            for j in range(c):
                row, col = divmod(x, m)
                new[i][j] =  matrix[row][col]
                x += 1
        return new