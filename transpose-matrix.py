class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        
        new = []
        for i in range(len(matrix[0])):
            temp = []
            for j in range(len(matrix)):
                temp.append(matrix[j][i])
            new.append(temp)
        return new