N = int(input())
SCV_hp = list(map(int, input().split()))

import itertools

dp = [[[-1] * 61 for _ in range(61)] for _ in range(61)]


def sol(a, b, c):
    if a<0:
        return sol(0, b, c)
    if b<0:
        return sol(a, 0, c)
    if c<0:
        return sol(a, b, 0)
    if a==0 and b==0 and c==0:
        return 0
    if dp[a][b][c] != -1:
        return dp[a][b][c]
    dp[a][b][c] = 9999999
    for k in list(itertools.permutations([1, 3, 9])):
        dp[a][b][c] = min(dp[a][b][c], sol(a-k[0], b-k[1], c-k[2]))
    dp[a][b][c] += 1
    return dp[a][b][c]

scv = [0, 0, 0]
for i in range(len(SCV_hp)):
    scv[i] = SCV_hp[i]

print(sol(scv[0], scv[1], scv[2]))