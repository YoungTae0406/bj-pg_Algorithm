def solution(maps):
    answer = []
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    visited = []
    for _ in range(len(maps)):  # visited 셋팅
        temp = []
        for _ in range(len(maps[0])):
            temp.append(False)
        visited.append(temp)

    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if not visited[i][j] and not maps[i][j] == 'X':  # 방문 안했고 바다가 아니라면
                q = [(i, j)]
                sum = 0
                visited[i][j] = True
                while q:
                    temp_x, temp_y = q.pop(0)
                    sum += int(maps[temp_x][temp_y])

                    for k in range(4):
                        nx, ny = temp_x + dx[k], temp_y + dy[k]
                        if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]):
                            if not visited[nx][ny] and not maps[nx][ny] == 'X':
                                q.append((nx, ny))
                                visited[nx][ny] = True
            else:
                continue
            answer.append(int(sum))

    if len(answer) != 0:
        answer.sort()
    else:
        answer.append(-1)

    return answer