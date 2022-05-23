import sys

t = int(sys.stdin.readline())
lst = []
for _ in range(t):
    lst.append(int(sys.stdin.readline()))

dp = [0] * 5001
dp[0] = 1
for i in range(2, 5001, 2):
    for j in range(2, i + 1, 2):
        dp[i] += (dp[j - 2] * dp[i - j]) % 1000000007

for i in lst:
    print(dp[i] % 1000000007)

