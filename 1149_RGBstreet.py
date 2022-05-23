n = int(input())
arr_cost = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * 3 for _ in range(n)]

dp[0][0] = arr_cost[0][0]
dp[0][1] = arr_cost[0][1]
dp[0][2] = arr_cost[0][2]

for i in range(1, n):
    a = arr_cost[i][0] + dp[i-1][1]
    b = arr_cost[i][0] + dp[i-1][2]
    dp[i][0] = min(a, b)

    c = arr_cost[i][1] + dp[i - 1][0]
    d = arr_cost[i][1] + dp[i - 1][2]
    dp[i][1] = min(c, d)

    e = arr_cost[i][2] + dp[i - 1][0]
    f = arr_cost[i][2] + dp[i - 1][1]
    dp[i][2] = min(e, f)

print(min(dp[n-1]))