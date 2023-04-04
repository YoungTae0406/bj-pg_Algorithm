import copy
n = int(input())
board_map = [list(map(int, input().split())) for _ in range(n)]

left = [0, -1]
right = [0, 1]
up = [-1, 0]
down = [1, 0]

direction = [left, right, up, down]

# 마지노선을 만들고 if문으로 비어있으면 j번째가 바로 이동
# 같으면 2배, 그 외의 경우 예를 들어 top과 j에 숫자가 있지만 같지는 않은 경우
# j 자리에 그대로 놓는다.
def move(temp_map, dir):
    if dir == left:
        for i in range(n):
            top = 0
            for j in range(1, n):
                if temp_map[i][j]:
                    tmp = temp_map[i][j]
                    temp_map[i][j] = 0
                    if temp_map[i][top] == 0:
                        temp_map[i][top] = tmp
                    elif temp_map[i][top] == tmp:
                        temp_map[i][top] *= 2
                        top += 1
                    else:
                        top += 1
                        temp_map[i][top] = tmp

    if dir == right:
        for i in range(n):
            top = n - 1
            for j in range(n - 2, -1, -1):
                if temp_map[i][j]:
                    tmp = temp_map[i][j]
                    temp_map[i][j] = 0
                    if temp_map[i][top] == 0:
                        temp_map[i][top] = tmp
                    elif temp_map[i][top] == tmp:
                        temp_map[i][top] = tmp * 2
                        top -= 1
                    else:
                        top -= 1
                        temp_map[i][top] = tmp

    if dir == up:
        for j in range(n):
            top = 0
            for i in range(1, n):
                if temp_map[i][j]:
                    tmp = temp_map[i][j]
                    temp_map[i][j] = 0
                    if temp_map[top][j] == 0:
                        temp_map[top][j] = tmp
                    elif temp_map[top][j] == tmp:
                        temp_map[top][j] = tmp * 2
                        top += 1
                    else:
                        top += 1
                        temp_map[top][j] = tmp

    if dir == down:
        for j in range(n):
            top = n - 1
            for i in range(n - 2, -1, -1):
                if temp_map[i][j]:
                    tmp = temp_map[i][j]
                    temp_map[i][j] = 0
                    if temp_map[top][j] == 0:
                        temp_map[top][j] = tmp
                    elif temp_map[top][j] == tmp:
                        temp_map[top][j] = tmp * 2
                        top -= 1
                    else:
                        top -= 1
                        temp_map[top][j] = tmp

    return temp_map

ans = 0
def req(cnt, tempmap):
    global ans
    if cnt == 5:
        for i in range(n):
            f = max(tempmap[i])
            ans = max(f, ans)
        return

    left_map = copy.deepcopy(tempmap)
    right_map = copy.deepcopy(tempmap)
    up_map = copy.deepcopy(tempmap)
    down_map = copy.deepcopy(tempmap)
    for k in range(4):
        d = direction[k]
        if d == left:
            req(cnt+1, move(left_map, left))

        if d == right:
            req(cnt+1, move(right_map, right))
        if d == up:
            req(cnt+1, move(up_map, up))

        if d == down:
            req(cnt+1, move(down_map, down))

#print(move(board_map, left))
req(0, board_map)
print(ans)