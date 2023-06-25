from collections import defaultdict

import sys
input = sys.stdin.readline


matrix = defaultdict(list)
n = int(input())
k = int(input())
graph = []

for i in range(k):
    graph.append(list(map(int, input().split())))
dic1 = defaultdict(list)
ans = []
for i in range(len(graph)):
    if graph[i][0] == 1:
        dic1[graph[i][1]].append(graph[i][2])
        dic1[graph[i][2]].append(graph[i][1])

for i in range(len(graph)):
    ans = []
    if graph[i][0] == 2:
        print(*dic1[graph[i][1]])
