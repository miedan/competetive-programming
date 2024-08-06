class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        def check_row(row):
            d= defaultdict(int)
            for i in range(9):
                if board[row][i] != '.':
                    d[board[row][i]] += 1
                    if d[board[row][i]] > 1:
                        print("row", d)
                        return False
                        
          
                
            return True
            

        def check_col(col):
            d = defaultdict(int)

            for i in range(9):
                if board[i][col] != '.':
                    d[board[i][col]] += 1
                    if d[board[i][col]] > 1:
                        print("col", d)
                        return False
            return True

        def check_grid(row, col):
            d = defaultdict(int)
            for r in range(row, row + 3):
                for c in range(col, col+3):
                    if board[r][c] != '.':
                        d[board[r][c]] += 1
                        if d[board[r][c]] > 1:
                            print("grid", d)
                            return False

            return True

        for i in range(9):
            if not check_row(i) or not check_col(i):
                print("cr")
                return False

        for i in range(0,9,3):

            for j in range(0,9,3):
                if not check_grid(i,j):
                    print("gr")
                    return False
        return True

       

            
        