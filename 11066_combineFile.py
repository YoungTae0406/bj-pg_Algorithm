import sys
test_case = int(sys.stdin.readline())

def sol(i, j):
    if i == j:
        return 0
    if dp[i][j] != -1:
        return dp[i][j]
    ans = dp[i][j]
    ee = sum(dp[i:j+1])
    for k in range(i, j):
        temp = sol(i, k) + sol(k+1, j) + ee
        if ans == -1 or ans > temp:
            ans = temp
    dp[i][j] = ans
    return ans


for _ in range(test_case):
    num_file = int(sys.stdin.readline())
    cost = list(map(int, sys.stdin.readline().split()))
    dp = [[-1] * num_file for _ in range(num_file)]
    print(sol(0, num_file-1))
