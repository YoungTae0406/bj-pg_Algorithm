from collections import deque

N, M, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
move = [[1, 0], [0, 1], [-1, 0], [0, -1]]

def rotate():
    q = deque()
    for depth in range(min(N, M) // 2):
        r = c = depth

        for dr, dc in move:
            while True:
                nr = r + dr
                nc = c + dc
                if depth <= nr < N - depth and depth <= nc < M - depth:
                    q.append(arr[r][c])
                    r = nr
                    c = nc
                else:
                    break

        for _ in range(R % ((N - depth * 2) * 2 + (M - depth * 2) * 2 - 4)):
            q.appendleft(q.pop())

        for dr, dc in move:
            while True:
                nr = r + dr
                nc = c + dc
                if depth <= nr < N - depth and depth <= nc < M - depth:
                    arr[r][c] = q.popleft()
                    r = nr
                    c = nc
                else:
                    break


rotate()
for i in range(N):
    for j in range(M):
        print(arr[i][j], end=" ")
    print()