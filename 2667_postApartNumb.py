from collections import deque
import sys
n = int(input())
maap = [list(map(str, (sys.stdin.readline().strip()))) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(start):
    q = deque()
    q.append(start)
    visited[start[0]][start[1]] = 1
    num = 1
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < n:
                if visited[nx][ny] == 0 and maap[nx][ny] == '1':
                    q.append((nx, ny))
                    visited[nx][ny] = visited[x][y]
                    num += 1
    return num


numa = 0
num_ans = []
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0 and maap[i][j] == '1':
            numa += 1
            num_ans.append(bfs((i, j)))
print(numa)
num_ans.sort()
for k in num_ans:
    print(k)

