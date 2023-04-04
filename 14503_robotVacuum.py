from collections import deque
n, m = map(int, input().split())
r, c, d = map(int, input().split())
mapArr = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
cnt = 1

#
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

visited[r][c] = 1

while 1:
    flag = False
    for _ in range(4):
        nx = r + dx[(d+3) % 4]
        ny = c + dy[(d+3) % 4]
        d = (d + 3) % 4
        if 0 <= nx < n and 0 <= ny < m:
            if visited[nx][ny] == 0 and mapArr[nx][ny] == 0:
                visited[nx][ny] = 1
                cnt += 1
                r = nx
                c = ny
                flag = True
                break
    if not flag:
        if mapArr[r-dx[(d)]][c-dy[(d)]] == 1:
            print(cnt)
            break
        else:
            r = r - dx[(d)]
            c = c - dy[(d)]


