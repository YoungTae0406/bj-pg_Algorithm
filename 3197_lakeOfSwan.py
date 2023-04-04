import sys
from collections import deque
# 얼음은 하루마다 녹고 물과 접촉한 부분만 녹는다.
# 며칠이 지나야 백조들이 만날 수 있는가
r, c = map(int, input().split())
lake = []; swan = []
water = deque(); temp_water = deque()
q, temp_q = deque(), deque()
visitedWater = [[0] * c for _ in range(r)]
visited = [[0] * c for _ in range(r)]

for i in range(r):
    a = list(input().strip())
    lake.append(a)
    for j in range(c):
        if a[j] == '.':
            water.append((i, j))
            visitedWater[i][j] = 1
        elif a[j] == 'L':
            swan.append((i, j))
            water.append((i, j))

x1, y1 = swan[0]
x2, y2 = swan[1]
q.append(swan[0])
lake[x1][y1], lake[x2][y2], visited[x1][y1] = '.', '.', 1
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
cnt = 0
# 백조 중 한마리를 water에 넣고 water과 같이 움직이며 나머지 백조를 찾는다.
# 물이랑 백조를 같이 넣자. 물로 얼음을 녹이고 녹여진 얼음을 water로 업데이트한다.
# 녹이면서 백조를 만날 수 있는지 확인

def melt():
    while water:
        x, y = water.popleft()
        if lake[x][y] == 'X':
            #print(x, y)
            lake[x][y] = '.'
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < r and 0 <= ny < c:
                if not visitedWater[nx][ny]:
                    if lake[nx][ny] == 'X':
                        temp_water.append((nx, ny))
                    else:
                        water.append((nx, ny))
                    visitedWater[nx][ny] = 1

def bfs():
    while q:
        x, y = q.popleft()
        if x == x2 and y == y2:
            return True
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < r and 0 <= ny < c:
                if not visited[nx][ny]:
                    if lake[nx][ny] == '.':
                        q.append((nx, ny))
                    else:
                        temp_q.append((nx, ny))
                    visited[nx][ny] = 1
    return False

while True:
    melt()
    if bfs():
        print(cnt)
        break
    q, water = temp_q, temp_water
    temp_q, temp_water = deque(), deque()
    cnt += 1