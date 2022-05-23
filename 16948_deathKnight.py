import sys
from collections import deque

N = int(sys.stdin.readline())
rone, cone, rtwo, ctwo = map(int, sys.stdin.readline().split())

possible_move_r = [-2, -2, 0, 0, 2, 2]
possible_move_c = [-1, 1, -2, 2, -1, 1]
visited = [[-1] * N for _ in range(N)]

def sol(r, c):
    q = deque()
    q.append((r, c))
    visited[r][c] = 0
    while q:
        temp_r, temp_c = q.popleft()

        for k in range(6):
            next_r = temp_r + possible_move_r[k]
            next_c = temp_c + possible_move_c[k]
            if 0 <= next_r < N and 0 <= next_c < N:
                if visited[next_r][next_c] == -1:
                    q.append((next_r, next_c))
                    visited[next_r][next_c] = visited[temp_r][temp_c] +1


sol(rone, cone)
print(visited[rtwo][ctwo])

