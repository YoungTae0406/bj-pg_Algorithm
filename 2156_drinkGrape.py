import sys
n = int(input())
grape = [0] + [int(sys.stdin.readline()) for _ in range(n)]
dp = [0] + [0] * n

if n == 1:
    dp[1] = grape[1]
    print(dp[1])
    exit()
if n == 2:
    dp[2] = grape[1] + grape[2]
    print(dp[2])
    exit()
else:
    dp[1] = grape[1]
    dp[2] = grape[1] + grape[2]

    for i in range(3, n+1):
        a = grape[i-1] + grape[i] + dp[i-3]
        b = grape[i] + dp[i-2]
        c = dp[i-1]
        dp[i] = max(a, b, c)
print(max(dp))
