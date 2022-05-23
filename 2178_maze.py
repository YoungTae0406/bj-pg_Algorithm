n, m = map(int, input().split())
maze= []
for _ in range(n):
    temp = input()
    maze.append(temp)

visited = [[1] * m for _ in range(n)]

dn = [0, 0, 1, -1]
dm = [1, -1, 0, 0]
queue = [[0,0]]

while queue:
    temp_n, temp_m = queue.pop(0)
    if temp_n == n-1 and temp_m == m-1:
        print(visited[temp_n][temp_m])
        break
    for i in range(4):
        go_n = temp_n + dn[i]
        go_m = temp_m + dm[i]
        if 1 <= go_n+1 <= n and 1 <= go_m+1 <= m:
            if visited[go_n][go_m] == 1 and maze[go_n][go_m] == '1':
                visited[go_n][go_m] = visited[temp_n][temp_m] + 1
                queue.append((go_n, go_m))
