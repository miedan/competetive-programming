class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 1:
            return [0]

        graph = defaultdict(list)
        incoming = [0 for _ in range(n)]

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
            incoming[a] += 1
            incoming[b] += 1

        leaves = deque()

        for index, count in enumerate(incoming):
            if count == 1:
                leaves.append(index)

        nodes = n
        

        while nodes > 2:
            leaves_size = len(leaves)
            nodes -= leaves_size

            for _ in range(leaves_size):
                leaf = leaves.popleft()

                for neighbor in graph[leaf]:
                    incoming[neighbor] -= 1

                    if incoming[neighbor] == 1:
                        leaves.append(neighbor)
                        

        return list(leaves)