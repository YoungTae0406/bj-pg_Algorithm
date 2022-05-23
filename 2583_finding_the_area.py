#https://www.acmicpc.net/problem/2583
import copy
def bfs(start):
    queue = [start]
    count2 = 0
    while queue:
        temp_y, temp_x = queue.pop(0)
        if visited[temp_y][temp_x] == 0:
            visited[temp_y][temp_x] = 1
            count2 += 1
            for i in range(4):
                go_x = temp_x + dx[i]
                go_y = temp_y + dy[i]
                if 0 <= go_x < weight and 0<= go_y < height :
                    if visited[go_y][go_x] == 0:
                        queue.append([go_y, go_x])
    isolated_count.append(count2)
    return 1

height, weight, num_square = map(int, input().split())
square_area = [[0] * weight for _ in range(height)]
for _ in range(num_square):
    weight_x, weight_y, height_x, height_y = map(int, input().split())
    for i in range(height_y - weight_y):
        for j in range(height_x - weight_x):
            square_area[i+weight_y][j+weight_x] = 1
visited = copy.deepcopy(square_area)
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
count = 0
isolated_count = []

for i in range(height):
    for j in range(weight):
        if square_area[i][j] == 0 and visited[i][j] == 0:
            count += bfs([i, j])

print(count)
isolated_count.sort()
for temp in isolated_count:
    print(temp, end=" ")

