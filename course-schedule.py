class Solution:
    def canFinish(self, numcourses: int, prerequisites: List[List[int]]) -> bool:

        graph = defaultdict(list)
        incoming = [0] * numcourses
        

        for a, b in prerequisites:
            graph[b].append(a)
            incoming[a] += 1
        que = deque([])
        for index, count in enumerate(incoming):
            if count == 0:
                que.append(index)

        store = []
        while que:
            now = que.popleft()
            store.append(now)
            for course in graph[now]:
                incoming[course] -= 1

                if incoming[course] == 0:
                    que.append(course)

        if len(store) != numcourses:
            return False

        return True