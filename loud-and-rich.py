class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:

        graph = defaultdict(list)
        output = [i for i in range(len(quiet))]
        cnt = [0 for _ in range(len(quiet))]
        que = deque()

        for a, b in richer:
            graph[a].append(b)
            cnt[b] += 1
        
        
        for index, count in enumerate(cnt):
            if count == 0:
                que.append(index)

        while que:
            now = que.popleft()
            

            for i in graph[now]:
                if(quiet[output[now]] <= quiet[output[i]]):
                    output[i] = output[now]
                    

                cnt[i] -= 1
                if cnt[i] == 0:
                    que.append(i)
        return output