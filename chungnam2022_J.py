import sys
from math import inf
n = int(input())
arr = list(map(int, sys.stdin.readline().split()))

ans = 0
curmmin = float(inf)

for i in range(len(arr)):
    if arr[i] > curmmin:
        continue

    for j in range(i+1, len(arr)):
        if arr[i] >= arr[j]:
            curmmin = arr[j]
            break
        else:
            ans = max(ans, arr[j] - arr[i])

print(ans)