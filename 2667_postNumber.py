def bfs(start):
    queue = [start]
    count2 = 0
    while queue:
        temp_x, temp_y = queue.pop(0)
        if visited[temp_y][temp_x] == 1 and map[temp_y][temp_x] == '1':
            visited[temp_y][temp_x] = 0
            count2 += 1
            for i in range(4):
                go_x = temp_x + dx[i]
                go_y = temp_y + dy[i]
                if 0 <= go_x < N and 0 <= go_y < N:
                    if visited[go_y][go_x] == 1:
                        queue.append([go_x, go_y])
    soort.append(count2)
    return 1

N = int(input())
map = []
for _ in range(N):
    a = input()
    map.append(a)

visited = [[1] * N for _ in range(N)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
count = 0
soort = []
for i in range(N):
    for j in range(N):
        if map[i][j] == '1' and visited[i][j] == 1:
            count += bfs([j, i])

print(count)
soort.sort()
for i in range(len(soort)):
    print(soort[i])