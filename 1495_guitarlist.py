import sys

N, S, M = map(int, sys.stdin.readline().split())
Volume = [0] + list(map(int, sys.stdin.readline().split()))

dp = [[0] * (M+1) for _ in range(N+1)]
dp[0][S] = 1

for i in range(N):
    for j in range(M+1):
        if dp[i][j] == 0:
            continue
        if j-Volume[i+1] >= 0:
            dp[i+1][j-Volume[i+1]] = 1
        if j+Volume[i+1] <= M:
            dp[i+1][j+Volume[i+1]] = 1

ans = -1
for j in range(M+1):
    if dp[N][j] == 1:
        ans = j
print(ans)