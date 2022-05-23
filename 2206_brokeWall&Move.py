'''
import sys
import copy
from collections import deque
N, M = map(int, sys.stdin.readline().split())
mapp = [list(map(int, (sys.stdin.readline().strip()))) for _ in range(N)]
visited = [[-1] * M for _ in range(N)]
wall = []
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for i in range(N):
    for j in range(M):
        if mapp[i][j] == 1:
            wall.append((i, j))


def sol(i, j):
    q = deque()
    q. append((i, j))
    temp_mapp[i][j] = 1
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x+dx[k]
            ny = y+dy[k]
            if 0 <= nx < N and 0<= ny < M:
                if temp_mapp[nx][ny] == 0:
                    q.append((nx, ny))
                    temp_mapp[nx][ny] = int(temp_mapp[x][y]) + 1


ans = 10000
for i, j in wall:
    temp_mapp = copy.deepcopy(mapp)
    temp_mapp[i][j] = 0
    sol(0, 0)
    if temp_mapp[N-1][M-1] < ans:
        ans = temp_mapp[N-1][M-1]

if temp_mapp[N-1][M-1] == 0:
    print(-1)
else:
    print(ans)

'''

from collections import deque
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
n, m = map(int, input().split())
mapp = [list(map(int, list(input()))) for _ in range(n)]
dist = [[[0]*2 for j in range(m)] for i in range(n)]

q = deque()
q.append((0, 0, 0))
dist[0][0][0] = 1

while q:
    x, y, z = q.popleft()
    for k in range(4):
        nx, ny = x+dx[k], y+dy[k]
        if 0<= nx < n and 0<= ny < m:
            if mapp[nx][ny] == 0 and dist[nx][ny][z] == 0:
                dist[nx][ny][z] = dist[x][y][z] + 1
                q.append((nx, ny, z))
            if z == 0 and mapp[nx][ny] == 1 and dist[nx][ny][z+1] == 0:
                dist[nx][ny][z+1] = dist[x][y][z] + 1
                q.append((nx, ny, z+1))

if dist[n-1][m-1][0] != 0 and dist[n-1][m-1][1] != 0: #전체에 값이 존재
    print(min(dist[n-1][m-1]))
elif dist[n-1][m-1][0] != 0:
    print(dist[n-1][m-1][0])
elif dist[n-1][m-1][1] != 0:
    print(dist[n-1][m-1][1])
else: #count(0)가 2개
    print(-1)
