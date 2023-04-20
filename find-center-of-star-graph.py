class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:

        for i in range(len(edges[0])):
            if edges[0][i] in edges[1]:
                return edges [0][i]