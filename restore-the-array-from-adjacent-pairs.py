class Solution:
    def restoreArray(self, adj: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        output = []
        visited = set()

        
        for a, b in adj:
            graph[a].append(b)
            graph[b].append(a)

        start = None
        for i in graph:
            if len(graph[i]) == 1:
                start = i
                break

        while start is not None:
            output.append(start)
            visited.add(start)
            start = None

            for neighbour in graph[output[-1]]:
                if neighbour not in visited:
                    start = neighbour
                    break

        return output