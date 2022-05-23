'''
import sys
sys.setrecursionlimit(1000000)
n, m = map(int, input().split())
candy_map = [list(map(int, input().split())) for _ in range(n)]
ans = 0

dx = [1, 0, 1]
dy = [0, 1, 1]

def sol(x, y, candy):
    global ans
    if x == n-1 and y == m-1:
        candy += candy_map[x][y]
        ans = max(ans, candy)
        return ans
    for k in range(3):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < n and 0 <= ny < m:
            candy += candy_map[x][y]

            #print(x, y, nx, ny, candy)
            ans = sol(nx, ny, candy)
            candy -= candy_map[x][y]

            #print(ans)
    return ans

print(sol(0, 0, 0))
'''

n, m = map(int, input().split())
dp = [[0] * (m+1)] * (n+1)
candy = []

for i in range(n):
    candy.append(list(map(int, input().split())))

for i in range(1, n+1):
    for j in range(1, m+1):
        dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + candy[i-1][j-1]

print(dp[n][m])
