from collections import deque

n, m = map(int, input().split())
cctv = []
wall = []
arr = []
ans = n * m

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

left = [-1, 0]
right = [1, 0]
up = [0, -1]
down = [0, 1]
two = [[left, right], [up, down]]
three = [[up, right], [right, down], [down, left], [left, up]]
four = [[left, up, right], [up, right, down], [right, down, left], [down, left, up]]
five = [[left, up, right, down]]

visited1 = [[0] * m for _ in range(n)]

for i in range(n):
    arr.append(list(map(int, input().split())))
    for j in range(m):
        if arr[i][j] == 6:
            wall.append((i, j))
            ans -= 1
        if 1 <= arr[i][j] <= 5:
            cctv.append((arr[i][j], i, j))
            ans -= 1

anslist = []
#print(wall, cctv, arr)

def cctvlocate(cctv, idx):
    global anslist
    ans2 = n*m - len(wall)
    if idx == len(cctv):
        for i in range(n):
            for j in range(m):
                if visited1[i][j] != 0:
                    ans2 -= 1
        anslist.append(ans2)
        return

    num, i, j = cctv[idx]

    if num == 1:
        visited2 = []
        q = deque()

        for k in range(4):
            q.append((i, j))
            dir_x = dx[k]
            dir_y = dy[k]
            while q:
                temp_x, temp_y = q.popleft()
                visited1[temp_x][temp_y] += 1
                x, y = temp_x+dir_x, temp_y+dir_y
                if 0 <= x < n and 0<= y < m:
                    if arr[x][y] != 6:
                        visited2.append((x, y))
                        q.append((x, y))


            cctvlocate(cctv, idx+1)
            for re_x, re_y in visited2:
                visited1[re_x][re_y] -= 1
            visited2 = []

    elif num == 2:
        visited2 = []
        q = deque()
        for dir1, dir2 in two:
            dir1_x, dir1_y = dir1[0], dir1[1]
            dir2_x, dir2_y = dir2[0], dir2[1]
            temp_dir = []
            temp_dir.append([dir1_x, dir1_y])
            temp_dir.append([dir2_x, dir2_y])

            for k in range(2):
                q.append((i, j))
                dir_x = temp_dir[k][0]
                dir_y = temp_dir[k][1]
                while q:
                    temp_x, temp_y = q.popleft()
                    visited1[temp_x][temp_y] += 1
                    x, y = temp_x + dir_x, temp_y + dir_y
                    if 0 <= x < n and 0 <= y < m:
                        if arr[x][y] != 6:
                            visited2.append((x, y))
                            q.append((x, y))

            cctvlocate(cctv, idx + 1)
            for re_x, re_y in visited2:
                visited1[re_x][re_y] -= 1
            visited2 = []

    elif num == 3:
        visited2 = []
        q = deque()

        for dir1, dir2 in three:
            dir1_x, dir1_y = dir1[0], dir1[1]
            dir2_x, dir2_y = dir2[0], dir2[1]
            temp_dir = []
            temp_dir.append([dir1_x, dir1_y])
            temp_dir.append([dir2_x, dir2_y])

            for k in range(2):
                q.append((i, j))
                dir_x = temp_dir[k][0]
                dir_y = temp_dir[k][1]
                while q:
                    temp_x, temp_y = q.popleft()
                    visited1[temp_x][temp_y] += 1
                    x, y = temp_x + dir_x, temp_y + dir_y
                    if 0 <= x < n and 0 <= y < m:
                        if arr[x][y] != 6:
                            visited2.append((x, y))
                            q.append((x, y))

            cctvlocate(cctv, idx + 1)
            for re_x, re_y in visited2:
                visited1[re_x][re_y] -= 1
            visited2 = []

    elif num == 4:
        visited2 = []
        q = deque()

        for dir1, dir2, dir3 in four:
            dir1_x, dir1_y = dir1[0], dir1[1]
            dir2_x, dir2_y = dir2[0], dir2[1]
            dir3_x, dir3_y = dir3[0], dir3[1]
            temp_dir = []
            temp_dir.append([dir1_x, dir1_y])
            temp_dir.append([dir2_x, dir2_y])
            temp_dir.append([dir3_x, dir3_y])

            for k in range(3):
                q.append((i, j))
                dir_x = temp_dir[k][0]
                dir_y = temp_dir[k][1]
                while q:
                    temp_x, temp_y = q.popleft()
                    x, y = temp_x + dir_x, temp_y + dir_y
                    visited1[temp_x][temp_y] += 1
                    if 0 <= x < n and 0 <= y < m:
                        if arr[x][y] != 6:
                            visited2.append((x, y))
                            q.append((x, y))

            cctvlocate(cctv, idx + 1)
            for re_x, re_y in visited2:
                visited1[re_x][re_y] -= 1
            visited2 = []

    elif num == 5:
        visited2 = []
        q = deque()
        for dir1, dir2, dir3, dir4 in five:
            dir1_x, dir1_y = dir1[0], dir1[1]
            dir2_x, dir2_y = dir2[0], dir2[1]
            dir3_x, dir3_y = dir3[0], dir3[1]
            dir4_x, dir4_y = dir4[0], dir4[1]
            temp_dir = []
            temp_dir.append([dir1_x, dir1_y])
            temp_dir.append([dir2_x, dir2_y])
            temp_dir.append([dir3_x, dir3_y])
            temp_dir.append([dir4_x, dir4_y])

            for k in range(4):
                q.append((i, j))
                dir_x = temp_dir[k][0]
                dir_y = temp_dir[k][1]
                while q:
                    temp_x, temp_y = q.popleft()
                    x, y = temp_x + dir_x, temp_y + dir_y
                    visited1[temp_x][temp_y] += 1
                    if 0 <= x < n and 0 <= y < m:
                        if arr[x][y] != 6:
                            visited2.append((x, y))
                            q.append((x, y))

            cctvlocate(cctv, idx + 1)
            for re_x, re_y in visited2:
                visited1[re_x][re_y] -= 1
            visited2 = []

cctvlocate(cctv, 0)
print(min(anslist))