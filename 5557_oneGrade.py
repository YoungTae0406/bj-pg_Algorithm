import sys
n = int(input())
num = list(map(int, sys.stdin.readline().split()))
goal = num[-1]
dp = [[0] * 21 for _ in range(n-1)]
num = num[:-1]
dp[0][num[0]] = 1

for i in range(1, n-1):
    for j in range(21):
        if j-num[i] >= 0:
            dp[i][j] += dp[i-1][j-num[i]]
        if j+num[i] <= 20:
            dp[i][j] += dp[i-1][j+num[i]]
print(dp[n-2][goal])

