import sys
from collections import deque
m, n, h = map(int, input().split())
tomato_map = [[list(map(int, sys.stdin.readline().split())) for _ in range(n)] for _ in range(h)]
dx = [0, 0, 1, -1, 0, 0]
dy = [1, -1, 0, 0, 0, 0]
dz = [0, 0, 0, 0, 1, -1]
visited = [[[-1] * m for _ in range(n)] for _ in range(h)]

def bfs(sta):
    q = deque()
    for i in range(len(sta)):
        q.append(sta[i])
        visited[sta[i][0]][sta[i][1]][sta[i][2]] += 1
        tomato_map[sta[i][0]][sta[i][1]][sta[i][2]] = 1
    while q:
        hei, x, y = q.popleft()

        for k in range(6):
            nx = x+dx[k]
            ny = y+dy[k]
            nh = hei+dz[k]
            if 0 <= nx < n and 0<= ny < m and 0<= nh < h:
                if visited[nh][nx][ny] == -1 and tomato_map[nh][nx][ny] == 0:
                    q.append([nh, nx, ny])
                    visited[nh][nx][ny] = visited[hei][x][y] + 1
                    tomato_map[nh][nx][ny] = 1

start = []
for k in range(h):
    for i in range(n):
        for j in range(m):
            if tomato_map[k][i][j] == 1:
                start.append([k, i, j])

bfs(start)
#print(*visited, sep = "\n")

ans = -2
ans2 = 0
for k in range(h):
    for i in range(n):
        for j in range(m):
            if tomato_map[k][i][j] == 0:
                ans2 = -1
            ans = max(visited[k][i][j], ans)

if ans == 0:
    print(0)
if ans > 0 and ans2 == 0:
    print(ans)
if ans2 == -1:
    print(ans2)