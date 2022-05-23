import sys

a = sys.stdin.readline().strip()
b = sys.stdin.readline().strip()

dp = [[0] * (len(b)+1) for _ in range(len(a)+1)]
a = " "+a
b = " "+b

for i in range(1, len(a)):

    for j in range(1, len(b)):
        if a[i] == b[j]:
            dp[i][j] = dp[i-1][j-1]+1
        else:
            dp[i][j] = 0

ans = -1
for i in dp:
    for j in i:
        if j > ans:
            ans = j
print(ans)