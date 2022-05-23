import sys
sys.setrecursionlimit(1000000)
n = int(sys.stdin.readline())
board = [sys.stdin.readline() for _ in range(n)]
dx = [-1, -1, 0, 0, 1, 1]
dy = [0, 1, 1, -1, -1, 0]
colorv = [[-1] * n for _ in range(n)]
ans = 0

def dfs(x, y, color):
    global ans
    colorv[x][y] = color
    ans = max(ans, 1)
    for k in range(6):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < n and 0 <= ny < n:
            if board[nx][ny] == 'X':
                if colorv[nx][ny] == -1:
                    dfs(nx, ny, 1-color)
                ans = max(ans, 2)
                if colorv[nx][ny] == color:
                    ans = max(ans, 3)

for i in range(n):
    for j in range(n):
        if board[i][j] == 'X' and colorv[i][j] == -1:
            dfs(i, j, 0)


print(ans)

