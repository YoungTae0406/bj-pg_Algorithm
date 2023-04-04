from collections import deque
n, l = map(int, input().split())
pro_map = [list(map(int, input().split())) for _ in range(n)]

# 양 끝으로 이동 2n번
# 경사로는 낮은 칸 그리고 l개가 연속된 칸에 놓을 수 있음.
# 낮은 칸과 높은 칸의 차이가 1

isRunway = [[False for _ in range(n)] for _ in range(n)]
l_walk = 1

right = [0, 1]
down = [1, 0]
def row_check(row): # 올라가는 경우랑 내려가는 경우
    global l_walk
    temp = pro_map[row][:]
    temp_isRunway = isRunway[row][:]
    q = deque()
    q.append((row, 0, temp[0])) # 위치정보, 지도의 높이

    while q:
        x, y, temp_h = q.popleft()
        nx, ny = x + right[0], y + right[1]
        if 0 <= ny < n and 0 <= nx < n:
            if temp_h == temp[ny]:
                q.append((nx, ny, temp[ny]))
                l_walk += 1
                continue
            elif temp_h -1 == temp[ny]: # 내려가는 경우
                flag = False
                for i in range(1, l+1):
                    if 0 <= y+i < n:
                        b = temp_isRunway[y+i]
                        c = temp[y+i]
                        if temp[y] -1 != c:
                            flag = True
                        if b:
                            flag = True
                    else: # l만큼 내려가는 경사로를 설치해야하는데 범위를 벗어났다는건
                        # 경사로를 설치할 장소가 없다는 것.
                        return False
                if not flag:
                    l_walk = 1
                    q.append((x, y+l, temp[y+l]))
                    for i in range(1, l + 1):
                        if 0 <= y + i < n:
                            temp_isRunway[y+i] = True
                else:
                    return False

            elif temp[ny] - 1 == temp_h: # 올라가는 경우
                if l_walk >= l:
                    flag = False
                    for j in range(l):
                        if 0 <= y-j < n:
                            if temp_isRunway[y-j]:
                                flag = True
                        else:
                            return False
                    if not flag:
                        l_walk = 1
                        q.append((nx, ny, temp[ny]))
                        for i in range(l):
                            temp_isRunway[y-i] = True
                    else:
                        return False # 이미 경사로가 놓여져 있음.

                else: # 경사로를 놓을 수 있는 공간이 없음.
                    return False

            else: # 다음 칸의 높이 차이가 2이상
                return False
    l_walk = 1
    return True

def col_check(col):
    global l_walk
    temp = []
    for i in range(n):
        temp.append(pro_map[i][col])
    temp_isRunway = []
    for i in range(n):
        temp_isRunway.append(isRunway[i][col])
    #print(temp, temp_isRunway)
    q = deque()
    q.append((0, col, temp[0]))  # 위치정보, 지도의 높이

    while q:
        x, y, temp_h = q.popleft()
        nx, ny = x + down[0], y + down[1]
        if 0 <= ny < n and 0 <= nx < n:
            if temp_h == temp[nx]:
                q.append((nx, ny, temp[nx]))
                l_walk += 1
                continue
            elif temp_h - 1 == temp[nx]:  # 내려가는 경우
                flag = False
                for i in range(1, l + 1):
                    if 0 <= x + i < n:
                        b = temp_isRunway[x + i]
                        c = temp[x + i]
                        if temp[x] - 1 != c:
                            flag = True
                        if b:
                            flag = True
                    else:  # l만큼 내려가는 경사로를 설치해야하는데 범위를 벗어났다는건
                        # 경사로를 설치할 장소가 없다는 것.
                        return False
                if not flag:
                    l_walk = 1
                    q.append((x + l, y, temp[x + l]))
                    for i in range(1, l + 1):
                        if 0 <= x + i < n:
                            temp_isRunway[x + i] = True
                else:
                    return False

            elif temp[nx] - 1 == temp_h:  # 올라가는 경우
                if l_walk >= l:
                    flag = False
                    for j in range(l):
                        if 0 <= x - j < n:
                            if temp_isRunway[x - j]:
                                flag = True
                        else:
                            return False
                    if not flag:
                        l_walk = 1
                        q.append((nx, ny, temp[nx]))
                        for i in range(l):
                            temp_isRunway[x - i] = True
                    else:
                        return False  # 이미 경사로가 놓여져 있음.

                else:  # 경사로를 놓을 수 있는 공간이 없음.
                    return False

            else:  # 다음 칸의 높이 차이가 2이상
                return False
    return True

cnt = 0
for i in range(n):
    if (row_check(i)):
        cnt += 1
    if (col_check(i)):
        cnt += 1

print(cnt)
