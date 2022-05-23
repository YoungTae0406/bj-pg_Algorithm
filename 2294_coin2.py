import sys
n, k = map(int, sys.stdin.readline().split())
dp = [10001] * (k+1)
dp[0] = 0
coin = []
for _ in range(n):
    coin.append(int(input()))

for c in coin:
    for p in range(c, k+1):
        if p-c >= 0:
            dp[p] = min(dp[p], dp[p-c]+1)

if dp[k] != 10001:
    print(dp[k])
else:
    print(-1)

