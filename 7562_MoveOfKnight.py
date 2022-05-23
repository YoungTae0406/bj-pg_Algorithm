from collections import deque

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[y][x] = 0
    while q:
        temp_x, temp_y = q.popleft()
        if temp_x == end[0] and temp_y == end[1]:
            print(visited[temp_y][temp_x])
            break
        for k in range(8):
            dx = temp_x + move_x[k]
            dy = temp_y + move_y[k]
            if 0 <= dx < chess_length and 0 <= dy < chess_length:
                if visited[dy][dx] == -1:
                    q.append((dx, dy))
                    visited[dy][dx] = visited[temp_y][temp_x] + 1


test_case = int(input())
while test_case:
    chess_length = int(input())
    start = list(map(int, input().split()))
    end = list(map(int, input().split()))

    move_x = [1, 2, 2, 1, -1, -2, -2, -1]
    move_y = [2, 1, -1, -2, -2, -1, 1, 2]
    visited = [[-1] * chess_length for _ in range(chess_length)]

    bfs(start[0], start[1])
    test_case -= 1
