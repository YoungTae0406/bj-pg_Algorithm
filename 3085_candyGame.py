n = int(input())
board = [list(input()) for _ in range(n)]

def check(board_):
    a = 0
    for i in range(n):
        cnt = 1
        for j in range(1, n):
            if board_[i][j-1] == board_[i][j]:
                cnt += 1
            else:
                cnt = 1
            a = max(a, cnt)
        cnt = 1
        for j in range(1, n):
            if board_[j][i] == board_[j-1][i]:
                cnt += 1
            else:
                cnt = 1
            a = max(a, cnt)

    return a

ans = 0
for i in range(n):
    for j in range(1, n):
        board[i][j-1], board[i][j] = board[i][j], board[i][j-1]
        c = check(board)
        ans = max(ans, c)
        board[i][j-1], board[i][j] = board[i][j], board[i][j-1]

    for j in range(1, n):
        board[j][i], board[j-1][i] = board[j-1][i], board[j][i]
        c = check(board)
        #print(c)
        ans = max(ans, c)
        board[j][i], board[j-1][i] = board[j-1][i], board[j][i]

print(ans)