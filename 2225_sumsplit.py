n, k = map(int, input().split())

dp = [[0] * (k+1) for _ in range(n+1)]
# dp[i][j] : i는 합, j는 합을 만드는데 사용한 정수

for i in range(0, n+1):
    dp[i][1] = 1

# dp[4][2] = dp[4][1] + dp[3][1] + dp[2][1] + dp[1][1] + dp[0][1]
# dp[4][3] = dp[4][2] + dp[3][2] + dp[2][2] + dp[1][2] + dp[0][2]

for p in range(2, k+1):
    for i in range(0, n+1):
        for j in range(0, i+1):
            dp[i][p] += dp[j][p-1]
            #dp[i][p] += dp[i-j][p-1] + 1


print(dp[n][k] % 1000000000)

