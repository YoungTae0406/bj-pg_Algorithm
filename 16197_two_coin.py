import sys
y, x = list(map(int, input().split()))
maap = [list(map(str, input())) for _ in range(y)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def sol(step, x1, y1, x2, y2):
    if step == 11:
        return -1
    fall1 = False
    fall2 = False
    if x1 < 0 or x1 >= x or y1 < 0 or y1 >= y:
        fall1 = True
    if x2 < 0 or x2 >= x or y2 < 0 or y2 >= y:
        fall2 = True
    if fall1 and fall2:
        return -1
    if fall1 or fall2:
        return step
    ans = -1
    for k in range(4):
        nx1, ny1 = x1 + dx[k], y1 + dy[k]
        nx2, ny2 = x2+dx[k], y2+dy[k]
        if 0 <= nx1 < x and 0 <= ny1 < y and maap[ny1][nx1] == "#":
            nx1, ny1 = x1, y1
        if 0 <= nx2 < x and 0 <= ny2 < y and maap[ny2][nx2] == "#":
            nx2, ny2 = x2, y2
        temp = sol(step+1, nx1, ny1, nx2, ny2)
        if temp == -1:
            continue
        if ans == -1 or ans > temp:
            ans = temp
    return ans
x1 = y1= x2= y2 = -1
for i in range(y):
    for j in range(x):
        if maap[i][j] == 'o':
            if y1 == -1:
                x1, y1 = j, i
            else:
                x2, y2 = j, i
            maap[i][j] = '.'
print(sol(0, x1, y1, x2, y2))