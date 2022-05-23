#https://www.acmicpc.net/problem/1012
def bfs(start):
    queue = [start]
    while queue:
        temp_x, temp_y = queue.pop(0)
        if visited[temp_y][temp_x] == 0:
            visited[temp_y][temp_x] = 1
            for n in range(4):
                go_x = temp_x + dx[n]
                go_y = temp_y + dy[n]
                if 0 <= go_x < cabbage_width and 0 <= go_y < cabbage_vertical and visited[go_y][go_x] == 0:
                    if cabbage_farm[go_y][go_x] == 1:
                        queue.append([go_x, go_y])
    return 1

test_case = int(input())
for case in range(test_case):
    cabbage_width, cabbage_vertical, cabbage_number = map(int, input().split())
    cabbage_farm = [[0] * cabbage_width for _ in range(cabbage_vertical)]
    visited = [[0] * cabbage_width for _ in range(cabbage_vertical)]
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    count = 0

    for i in range(cabbage_number):
        x, y = map(int, input().split())
        cabbage_farm[y][x] = 1

    for i in range(cabbage_vertical):
        for j in range(cabbage_width):
            if cabbage_farm[i][j] == 1 and visited[i][j] == 0:
                count += bfs([j, i])
    print(count)

