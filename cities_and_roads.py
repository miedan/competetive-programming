from collections import defaultdict

import sys
input = sys.stdin.readline


adjlist = defaultdict(list)
n = int(input())
graph = []

for i in range(n):
    graph.append(list(map(int, input().split())))
cities = 0
for i in range(len(graph)):
    for j in range(i, n):
        if graph[i][j] == 1:
            cities += 1
            
print(cities)
