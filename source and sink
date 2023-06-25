from collections import defaultdict

import sys
input = sys.stdin.readline

t = int(input())
matrix = defaultdict(list)

for i in range(t):
    row = list(map(int, input().split()))
    for j in range(len(row)):
        matrix[i].append(row[j])


n = len(matrix)

presink, source, sink = [], [], []

for i in range(n):
    count = 0
    for j in range(n):
        if matrix[i][j] == 1:
            count += 1 
            presink.append(j+1)
    if count == 0:
        sink.append(i+1)


for j in range(1, n+1):
    if j not in presink:
        source.append(j)
        

print(len(source), *source)
print(len(sink), *sink)
