import sys
from collections import deque

W, H = map(int, sys.stdin.readline().split())
# H가 세로
mapp = [list(map(str, sys.stdin.readline().strip())) for _ in range(H)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
startx = starty = endx = endy = -1
for i in range(H):
    for j in range(W):
        if mapp[i][j] == 'C':
            if startx == -1:
                startx, starty = i, j
            else:
                endx, endy = i, j

visited = [[-1] * W for _ in range(H)]
q = deque()
q.append((startx, starty))
visited[startx][starty] = 0

while q:
    x, y = q.popleft()
    for k in range(4):
        nx, ny = x+dx[k], y+dy[k]
        while 0 <= nx < H and 0 <= ny < W:
            if mapp[nx][ny] == "*":
                break
            if visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))
            nx += dx[k]
            ny += dy[k]

print(visited[endx][endy] - 1)


