import sys
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
n, m = map(int, input().split())
maap = [list(map(int, input().split())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]
ans = 0

def go(x, y, sum, cnt):
    if cnt == 4:
        global ans
        if ans < sum:
           ans = sum
        return
    if x < 0 or x >= n or y < 0 or y >= m:
        return
    if visited[x][y]:
        return
    visited[x][y] = True
    for k in range(4):
        go(x+dx[k], y+dy[k], sum+maap[x][y], cnt+1)
    visited[x][y] = False

for i in range(n):
    for j in range(m):
        go(i, j, 0, 0)
        # ㅗ ㅏ ㅓ ㅜ
        if j+2 < m:
            temp = maap[i][j] + maap[i][j+1] + maap[i][j+2]
            if i-1 >= 0:
                temp2 = temp + maap[i-1][j+1]
                if ans < temp2:
                    ans = temp2
            if i+1 < n:
                temp2 = temp + maap[i+1][j+1]
                if ans < temp2:
                    ans = temp2
        if i+2 < n:
            temp = maap[i][j] + maap[i+1][j] + maap[i+2][j]
            if j+1 < m:
                temp2 = temp + maap[i+1][j+1]
                if ans < temp2:
                    ans = temp2
            if j-1 >= 0:
                temp2 = temp + maap[i+1][j-1]
                if ans < temp2:
                    ans = temp2
print(ans)