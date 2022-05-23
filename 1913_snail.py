n = int(input())
num = int(input())

arr = [[0] * n for _ in range(n)]
total_cnt = n//2 + 1
start = n*n
ans_x = 0
ans_y = 0
for p in range(total_cnt):
    j_cnt = p
    i_cnt = n-p-1

    for i in range(n):
        if start == num:
            ans_y = i + 1
            ans_x = j_cnt + 1

        if arr[i][j_cnt] == 0:
            arr[i][j_cnt] = start
            start -= 1

    for j in range(n):
        if start == num:
            ans_y = i_cnt + 1
            ans_x = j + 1

        if arr[i_cnt][j] == 0:
            arr[i_cnt][j] = start
            start -= 1

    j_cnt = n-p-1
    i_cnt = p
    for i in range(n-1, -1, -1):
        if start == num:
            ans_y = i + 1
            ans_x = j_cnt + 1

        if arr[i][j_cnt] == 0:
            arr[i][j_cnt] = start
            start -= 1

    for j in range(n-1, -1, -1):
        if start == num:
            ans_y = i_cnt + 1
            ans_x = j + 1

        if arr[i_cnt][j] == 0:
            arr[i_cnt][j] = start
            start -= 1

for p in arr:
    print(*p)
print(ans_y, ans_x)
