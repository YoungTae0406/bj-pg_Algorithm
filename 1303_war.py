import sys

n, m = list(map(int, sys.stdin.readline().split()))
arr = [sys.stdin.readline().strip() for _ in range(m)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
visited = [[0] * n for _ in range(m)]
queue = [[0, 0]]
answer = [0, 0]

for i in range(m):
    for j in range(n):
        count = 0
        if visited[i][j] == 0:
            queue.append([i, j])
            while queue:
                x, y = queue.pop(0)
                if visited[x][y] == 0:
                    visited[x][y] = 1
                    count += 1
                else:
                    continue
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if nx < 0 or ny < 0 or nx >= m or ny >= n:
                        continue
                    if arr[x][y] == arr[nx][ny]:
                        queue.append([nx, ny])
            ans = count * count
            if arr[i][j] == 'W':
                answer[0] += ans
            else:
                answer[1] += ans

print(answer[0], answer[1])