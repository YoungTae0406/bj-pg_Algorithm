from collections import deque
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
n, m, brokecnt = map(int, input().split())
mapp = [list(map(int, list(input()))) for _ in range(n)]
dist = [[[0]*(brokecnt+1) for j in range(m)] for i in range(n)]
#print(mapp)

q = deque()
q.append((0, 0, 0))
dist[0][0][0] = 1

while q:
    x, y, z = q.popleft()
    for k in range(4):
        nx, ny = x+dx[k], y+dy[k]
        if 0 <= nx < n and 0 <= ny < m:
            if mapp[nx][ny] == 0 and dist[nx][ny][z] == 0:
                dist[nx][ny][z] = dist[x][y][z] + 1
                q.append((nx, ny, z))
            if z < brokecnt and mapp[nx][ny] == 1 and dist[nx][ny][z+1] == 0:
                dist[nx][ny][z+1] = dist[x][y][z] + 1
                q.append((nx, ny, z+1))


ans = -1
for i in range(brokecnt+1):
    if dist[n-1][m-1][i] == 0:
        continue
    if ans == -1:
        ans = dist[n-1][m-1][i]
    elif ans > dist[n-1][m-1][i]:
        ans = dist[n-1][m-1][i]
print(ans)
