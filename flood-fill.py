class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        start = image[sr][sc]
        def dfs(row,col):

            if  row >= len(image) or col >= len(image[0]) or  start != image[row][col] or image[row][col] == color or  min(row,col) < 0:
                return 

            image[row][col] = color

            dfs(row, col+1)
            dfs(row, col-1)
            dfs(row+1, col)  
            dfs(row-1, col)
            
        dfs(sr,sc)
        return image