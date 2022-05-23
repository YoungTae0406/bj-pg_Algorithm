#samsung sw problem
import sys
from collections import deque
input = sys.stdin.readline

def changeDir(d, dirC):
    if dirC == 'L':
        d = (d+1) % 4
    if dirC == 'D':
        d = (d-1) % 4
    return d

n = int(input())
k = int(input())
apple = [list(map(int, input().split())) for _ in range(k)]
board = [[0] * n for _ in range(n)]
for x, y in apple:
    board[x-1][y-1] = 1

l = int(input())
times = {}
for _ in range(l):
    t, di = list(map(str, input().split()))
    times[int(t)] = di

# right, up, left, down
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]


q = deque()
x, y = 0, 0
q.append([x, y])
time = 1
board[0][0] = 2
dirr = 0

while True:
    x = dx[dirr] + x
    y = dy[dirr] + y
    if 0<= x < n and 0<= y < n and board[x][y] != 2:
        if board[x][y] != 1:
            rx, ry = q.popleft()
            board[rx][ry] = 0
        board[x][y] = 2
        q.append([x, y])

        if time in times.keys():
            dirr = changeDir(dirr, times[time])
        time += 1
    else:
        print(time)
        break




