n = int(input())
# 네 군데로 분할하는데 그때마다 ( 를 추가, 재귀를 해야하는지 for문을 돌려 확인
# 다 같은 값인지를 확인하고 다르다면 재귀로 다시 4군데로 분할

display = [list(map(int, input())) for _ in range(n)]
def recur(x, y, size):
    check = display[x][y]
    for i in range(x, x+size):
        for j in range(y, y+size):
            if check != display[i][j]:
                check = -1
                break
    if check == -1:
        print("(", end='')
        size = size//2
        recur(x, y, size)
        recur(x, y+size, size)
        recur(x+size, y, size)
        recur(x+size, y+size, size)
        print(")", end='')

    elif check == 1:
        print("1", end='')
    else:
        print("0", end='')

recur(0, 0, n)

