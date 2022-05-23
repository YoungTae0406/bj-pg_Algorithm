import sys
from collections import deque
import copy
N = int(input())
mapp = [list(map(str, sys.stdin.readline().strip())) for _ in range(N)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
blindness_mapp = copy.deepcopy(mapp)

for i in range(N):
    for j in range(N):
        if blindness_mapp[i][j] == "G":
            blindness_mapp[i][j] = "R"

def bfs_colorblindess(i, j, color):
    q = deque()
    q.append((i, j))
    visited_blindness[i][j] = 1
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < N:
                if visited_blindness[nx][ny] == 0 and blindness_mapp[nx][ny]==color:
                    q.append((nx, ny))
                    visited_blindness[nx][ny] = visited_blindness[i][j] + 1


def bfs_normal(i, j, color):
    q = deque()
    q.append((i, j))
    visited_normal[i][j] = 1
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < N:
                if visited_normal[nx][ny] == 0 and mapp[nx][ny]==color:
                    q.append((nx, ny))
                    visited_normal[nx][ny] = visited_normal[i][j] + 1


visited_blindness = [[0] * N for _ in range(N)]
visited_normal = [[0] * N for _ in range(N)]

cnt_one = 0; cnt_two = 0
for i in range(N):
    for j in range(N):
        if visited_blindness[i][j] == 0:
            if blindness_mapp[i][j] == "R" :
                bfs_colorblindess(i, j, "R")
            elif blindness_mapp[i][j] == "B":
                bfs_colorblindess(i, j, "B")
            cnt_one += 1

for i in range(N):
    for j in range(N):
        if visited_normal[i][j] == 0:
            if mapp[i][j] == "R" :
                bfs_normal(i, j, "R")
            elif mapp[i][j] == "B":
                bfs_normal(i, j, "B")
            elif mapp[i][j] == "G":
                bfs_normal(i,j,"G")
            cnt_two += 1

print(cnt_two, cnt_one)
