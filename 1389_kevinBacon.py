import sys
input = sys.stdin.readline
n, m = map(int, input().split())
inf = 10**5
arr = [[inf] * (n+1) for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    arr[a][b] = 1
    arr[b][a] = 1

for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            arr[i][j] = 0

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            arr[i][j] = min(arr[i][k] + arr[k][j], arr[i][j])

miin = 10**7
for i in range(1, n+1):
    miin = min(sum(arr[i]), miin)

for i in range(1, n+1):
    if sum(arr[i]) == miin:
        print(i)
        break

