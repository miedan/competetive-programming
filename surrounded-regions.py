class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
       

        
        def dfs(i, j):
            if i < 0 or j < 0 or i == len(board) or j == len(board[0]) or board[i][j] != "O":
                return
            board[i][j] = "q"
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

            if not board:
                return
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O" and (i == 0 or j == 0 or i == m - 1 or j == n - 1):
                    dfs(i, j)
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "q":
                    board[i][j] = "O"

        return board