import sys
from collections import deque
N, M = map(int, sys.stdin.readline().split())
after = list(range(101))
dist = [-1] * 101

for _ in range(N+M):
    x, y = map(int, input().split())
    after[x] = y
dist[1] = 0
q = deque()
q.append(1)
while q:
    x = q.popleft()
    for i in range(1, 7):
        y = x+i
        if y > 100:
            continue
        y = after[y]
        if dist[y] == -1:
            dist[y] = dist[x] + 1
            q.append(y)
print(dist[100])


