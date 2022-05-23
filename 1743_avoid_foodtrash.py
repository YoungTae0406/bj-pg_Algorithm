import sys

def bfs(i, j):
    queue.append([i, j])
    t = 1
    visited[i][j] = 1
    while queue:
        x, y = queue.pop(0)
        for k in range(4):
            nx, ny = x + dx[k], y+dy[k]
            if 0 <= nx < n and 0 <= ny < m and entity[nx][ny] == 1 and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                queue.append((nx, ny))
                t += 1
    return t


n, m, k = list(map(int, sys.stdin.readline().split()))
trash = [list(map(int, sys.stdin.readline().split())) for i in range(k)]
visited = [[0] * m for _ in range(n)]
entity = [[0] * m for _ in range(n)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
for x, y in trash:
    entity[x-1][y-1] = 1

ans = 0
queue = []
for i in range(n):
    for j in range(m):
        if entity[i][j] == 1 and visited[i][j] == 0:
            res = bfs(i, j)
            if res > ans:
                ans = res

print(ans)



