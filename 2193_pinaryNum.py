n = int(input())
dp = [[0] * 2 for i in range(91)]
dp[1][0] = 0
dp[1][1] = 1

for i in range(2, 91):
    for j in range(2):
        if j == 0:
            dp[i][j] = dp[i-1][j] + dp[i-1][j+1]
                #print(i, j)
        if j == 1:
            dp[i][j] = dp[i-1][j-1]
                #print(i, j)

print(sum(dp[n]))