import sys
from collections import deque


def sol():
    global visited
    find_ice(arr_map)
    #print(ice_map)
    cnt = 0
    visited = [[0] * m for _ in range(n)]
    for x, y in ice_map:
        if arr_map[x][y] != 0 and visited[x][y] == 0:
            bfs(x, y)
            #print(arr_map)
            cnt += 1
    if cnt > 1:
        return True
    else:
        return False

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    while q:
        #print(q)
        x, y = q.popleft()
        for k in range(4):
            zero_cnt = 0
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < m:
                if arr_map[nx][ny] > 0 and visited[nx][ny] == 0:
                    q.append((nx, ny))
                    visited[nx][ny] = 1
                if arr_map[nx][ny] == 0 and visited[nx][ny] == 0:
                    zero_cnt += 1
                arr_map[x][y] -= zero_cnt
                if arr_map[x][y] < 0:
                    arr_map[x][y] = 0

def find_ice(mapp):
    global ice_map
    ice_map = []
    for i in range(len(mapp)):
        for j in range(len(mapp[0])):
            if mapp[i][j] > 0:
                ice_map.append((i, j))
    #print(ice_map)
    if len(ice_map) == 0:
        print(0)
        exit(0)


n, m = map(int, sys.stdin.readline().split())
arr_map = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
ice_map = []
time = 0
visited = [[0] * m for _ in range(n)]

while True:
    if not sol():
        time += 1
    else:
        print(time)
        break

