from collections import defaultdict
import sys
input = sys.stdin.readline

n, k  = list(map(int, input().split()))
 
arr = list(map(int, input().split()))
arr.sort()
 
if 0 < k < n:
    if arr[k-1] < arr[k]:
        print(arr[k-1])
    else:
        print(-1)
elif k == 0:
    print(arr[0]-1 or -1)
else:
    print(arr[-1])
