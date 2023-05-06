class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n, m = len(matrix), len(matrix[0])
        arr = []
        for i in range(n):
            for j in range(m):
                arr.append(matrix[i][j])
        heapify(arr)

        while k:
            now = heappop(arr)
            k -= 1
        return now