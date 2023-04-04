from collections import deque
r, c, numShark = map(int, input().split())
shark = []
fishing_board = [[deque() for _ in range(c)] for _ in range(r)]

for i in range(numShark):
    sr, sc, velo, direction, size = map(int, input().split())
    shark.append([sr, sc, velo, direction, size])
    fishing_board[sr-1][sc-1].append(shark[i])

#print(fishing_board)
fishedshark = 0 # 잡은 상어 크기의 합

# 낚시왕은 1초마다 오른쪽으로 한 칸 이동하고 그 열에서 가장 가까운 상어 낚시
# 상어가 이동
def get_direction(direction_inf): # 상어 방향 정보에 따른 나아갈 방향
    if direction_inf == 1: #위
        return [-1, 0]
    elif direction_inf == 2: #아래
        return [1, 0]
    elif direction_inf == 3: #오른쪽
        return [0, 1]
    else:                   # 왼쪽
        return [0, -1]

def moveShark(shark_r, shark_c, shark_velo, shark_dire): # 현재 위치에서 상어가
    # 끝까지 갈 수 있는지 확인하고 움직이기
    if shark_dire == 1 or shark_dire == 2: # 위, 아래
        # shark_velo랑 ismove랑 크기 비교를 해서 끝까지 갈 수 있는지 확인
        # 갈 수 있다면 shark_velo에서 ismove만큼을 빼고 끝까지 이동, 방향 바꾸기
        # 갈 수 없다면 ismove만큼을 방향대로 이동
        # 1초에 갈 수 있는 곳으로 이동시키고 리턴해야 하네

        while shark_velo > 0:
            dire_r, dire_c = get_direction(shark_dire)
            #print(shark_r, shark_c, shark_velo, shark_dire)
            if shark_dire == 1: # 위
                ismove = shark_r - 1
                if shark_velo > ismove:
                    shark_r = shark_r + (dire_r * ismove)
                    shark_c = shark_c + (dire_c * ismove)
                    shark_velo -= ismove
                    shark_dire += 1
                else:
                    ismove = shark_velo
                    shark_r = shark_r + (dire_r * ismove)
                    shark_c = shark_c + (dire_c * ismove)
                    return [shark_r, shark_c, shark_dire]

            elif shark_dire == 2: # 아래
                ismove = r - shark_r
                if shark_velo > ismove:
                    shark_r = shark_r + (dire_r * ismove)
                    shark_c = shark_c + (dire_c * ismove)
                    shark_velo -= ismove
                    shark_dire = 1
                else:
                    ismove = shark_velo
                    shark_r = shark_r + (dire_r * ismove)
                    shark_c = shark_c + (dire_c * ismove)
                    shark_velo = 0
                    return [shark_r, shark_c, shark_dire]
        return [shark_r, shark_c, shark_dire]

    elif shark_dire == 3 or shark_dire == 4: # 오른쪽 왼쪽
        while shark_velo > 0:
            dire_r, dire_c = get_direction(shark_dire)
            #print(shark_r, shark_c, shark_velo, shark_dire)
            if shark_dire == 3: # 오른쪽
                ismove = c - shark_c
                if shark_velo > ismove:
                    shark_r = shark_r + (dire_r * ismove)
                    shark_c = shark_c + (dire_c * ismove)
                    shark_velo -= ismove
                    shark_dire += 1
                else:
                    ismove = shark_velo
                    shark_r = shark_r + (dire_r * ismove)
                    shark_c = shark_c + (dire_c * ismove)
                    return [shark_r, shark_c, shark_dire]

            elif shark_dire == 4: # 왼쪽
                ismove = shark_c - 1
                if shark_velo > ismove:
                    shark_r = shark_r + (dire_r * ismove)
                    shark_c = shark_c + (dire_c * ismove)
                    shark_velo -= ismove
                    shark_dire = 3
                else:
                    ismove = shark_velo
                    shark_r = shark_r + (dire_r * ismove)
                    shark_c = shark_c + (dire_c * ismove)
                    return [shark_r, shark_c, shark_dire]
        return [shark_r, shark_c, shark_dire]

# 나머지와 몫을 구해서 상어의 움직임을 간단히 할 순 없어 보임.
# 한칸씩 이동하는건 비효율적이니 맨 끝까지 갈 수 있는지 확인하고 갈 수 있다면
# 맨 끝까지 한 번에 보내버리는 방식으로

for p in range(c):
    #print('-----'+str(p))
    for i in range(r): # fishing
        if len(fishing_board[i][p]) == 0:
            continue
        else:
            delete_shark = fishing_board[i][p][0]
            shark.remove(delete_shark)
            #print(fishing_board[i][p])
            fishing_board[i][p].remove(delete_shark)
            fishedshark += delete_shark[4]
            #print('fishing')
            break

    for j in range(len(shark)): # 상어들의 이동
        shark_r, shark_c, shark_velo, shark_dir, shark_size = shark[j]
        #print(shark[j])
        shark_nr, shark_nc, shark_ndir = moveShark(shark_r, shark_c, shark_velo, shark_dir)
        #print(shark_nr, shark_nc, shark_ndir, shark[j])
        shark[j] = [shark_nr, shark_nc, shark_velo, shark_ndir, shark_size]
        #print(shark[j])
    fishing_board = [[deque() for _ in range(c)] for _ in range(r)] # new
    willdelete = []
    for j in range(len(shark)):
        shark_r, shark_c, shark_velo, shark_dir, shark_size = shark[j]
        if len(fishing_board[shark_r-1][shark_c-1]) >= 1:
            #print('shark eat')
            if fishing_board[shark_r-1][shark_c-1][0][4] > shark_size:
                willdelete.append(shark[j])
                continue
            else:
                a = fishing_board[shark_r-1][shark_c-1].pop()
                willdelete.append(a)
                fishing_board[shark_r-1][shark_c-1].append(shark[j])
        else:
            fishing_board[shark_r-1][shark_c-1].append(shark[j])
    #print(willdelete)
    for i in range(len(willdelete)):
        shark.remove(willdelete[i])


print(fishedshark)

