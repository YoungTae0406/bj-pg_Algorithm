import sys
from collections import deque

N = int(sys.stdin.readline().strip())
mapp = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(i, j, size):
    dist = [[-1] * N for _ in range(N)]
    q = deque()
    q.append((i, j))
    dist[i][j] = 0
    ans = []

    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x+dx[k], y+dy[k]
            if 0 <= nx < N and 0<= ny < N and dist[nx][ny] == -1:
                move_ok = False
                eat = False
                if mapp[nx][ny] == 0:
                    move_ok = True
                elif size == mapp[nx][ny]:
                    move_ok = True
                elif size > mapp[nx][ny]:
                    move_ok = True
                    eat = True
                if move_ok:
                    q.append((nx, ny))
                    dist[nx][ny] = dist[x][y] +1
                    if eat:
                        ans.append((dist[nx][ny], nx, ny))
    if not ans:
        return None
    ans.sort()
    return ans[0]


shark_exp = 0
shark_size = 2
for i in range(N):
    for j in range(N):
        if mapp[i][j] == 9:
            x, y = i, j
            mapp[i][j] = 0

answer = 0
while True:
    fish = bfs(x, y, shark_size)
    if fish is None:
        break
    temp_dist, temp_x, temp_y = fish
    answer += temp_dist
    mapp[temp_x][temp_y] = 0
    shark_exp += 1
    if shark_size == shark_exp:
        shark_size += 1
        shark_exp = 0
    x, y = temp_x, temp_y
print(answer)


