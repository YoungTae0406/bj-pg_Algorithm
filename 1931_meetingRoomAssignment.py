import sys
n = int(input())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
arr.sort(key=lambda x: x[0])
arr.sort(key=lambda x: x[1])

last = 0
cnt = 0
for i, j in arr:
    if i >= last:
        cnt += 1
        last = j

print(cnt)
