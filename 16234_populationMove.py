import sys
from collections import deque
N, L, R = map(int, sys.stdin.readline().split())
peo = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

ans = 0

def bfs(l ,r):
    n = len(peo)
    visited = [[False] * N for _ in range(N)]
    ok = False

    for i in range(n):
        for j in range(n):
            if visited[i][j] == False:
                q = deque()
                q.append((i, j))
                visited[i][j] = True
                s = [(i, j)]
                total = peo[i][j]
                while q:
                    x, y = q.popleft()
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if 0 <= nx < N and 0 <= ny < N:
                            if visited[nx][ny] == False:
                                diff = abs(peo[nx][ny] - peo[x][y])
                                if l <= diff <= r:
                                    q.append((nx,ny))
                                    s.append((nx, ny))
                                    visited[nx][ny] = True
                                    ok = True
                                    total += peo[nx][ny]
                val = total // len(s)
                for x, y in s:
                    peo[x][y] = val

    return ok


while True:
    if bfs(L, R):
        ans += 1
    else:
        break

print(ans)