from collections import defaultdict

import sys
input = sys.stdin.readline


adjlist = defaultdict(list)
n = int(input())
graph = []

for i in range(n):
    graph.append(list(map(int, input().split())))

for i in range(len(graph)):
    for j in range(len(graph[i])):
        if graph[i][j] == 1:
            adjlist[i+1].append(j+1)
for i in adjlist:
    print(len(adjlist[i]), *(sorted(adjlist[i])))
