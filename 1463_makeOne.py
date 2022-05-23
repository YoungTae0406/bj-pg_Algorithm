import sys
n = int(sys.stdin.readline())
dp = [0] * 1000001
dp[1] = 0
dp[2] = 1
dp[3] = 1

for i in range(4, n+1):
    a = 10**6
    b = 10**6
    c = 10**6
    if i % 3 == 0:
        a = dp[i//3] + 1

    if i % 2 ==0:
        b = dp[i//2] + 1
    c = dp[i-1] + 1
    dp[i] = min(a, b, c)

print(dp[n])
