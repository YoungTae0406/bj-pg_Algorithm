import sys
from collections import deque
import copy
import itertools

N, M = map(int, sys.stdin.readline().split())
mapp = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
choice = []
virus = []

for i in range(N):
    for j in range(M):
        if mapp[i][j] == 0:
            choice.append((i, j))
        if mapp[i][j] == 2:
            virus.append((i, j))

def sol(i, j):
    q = deque()
    q.append((i, j))
    while q:
        temp_x, temp_y = q.popleft()

        for k in range(4):
            nx = temp_x + dx[k]
            ny = temp_y + dy[k]
            if 0<= nx < N and 0<= ny < M:
                if temp_mapp[nx][ny] == 0:
                    temp_mapp[nx][ny] = 2
                    q.append((nx, ny))


combi = itertools.combinations(choice, 3)
ans = []
for one, two, three in combi:
    temp_mapp = copy.deepcopy(mapp)
    cnt = 0
    temp_mapp[one[0]][one[1]] = 1
    temp_mapp[two[0]][two[1]] = 1
    temp_mapp[three[0]][three[1]] = 1
    for i, j in virus:
        sol(i, j)
    for i in range(N):
        for j in range(M):
            if temp_mapp[i][j] == 0:
                cnt += 1
    ans.append(cnt)
    temp_mapp[one[0]][one[1]] = 0
    temp_mapp[two[0]][two[1]] = 0
    temp_mapp[three[0]][three[1]] = 0

print(max(ans))


