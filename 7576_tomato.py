import sys
from collections import deque
m, n = map(int, input().split())
tomato_map = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
visited = [[-1] * m for _ in range(n)]

def bfs(sta):
    q = deque()
    for i in range(len(sta)):
        q.append(sta[i])
        visited[sta[i][0]][sta[i][1]] += 1
        tomato_map[sta[i][0]][sta[i][1]] = 1
    while q:
        x, y = q.popleft()

        for k in range(4):
            nx = x+dx[k]
            ny = y+dy[k]
            if 0 <= nx < n and 0<= ny < m:
                if visited[nx][ny] == -1 and tomato_map[nx][ny] == 0:
                    q.append([nx, ny])
                    visited[nx][ny] = visited[x][y] + 1
                    tomato_map[nx][ny] = 1

start = []
for i in range(n):
    for j in range(m):
        if tomato_map[i][j] == 1:
            start.append([i, j])

bfs(start)
#print(*visited, sep = "\n")

ans = -2
ans2 = 0
for i in range(n):
    for j in range(m):
        if tomato_map[i][j] == 0:
            ans2 = -1
        ans = max(visited[i][j], ans)

if ans == 0:
    print(0)
if ans > 0 and ans2 == 0:
    print(ans)
if ans2 == -1:
    print(ans2)