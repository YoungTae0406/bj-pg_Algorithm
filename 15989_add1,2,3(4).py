import sys
'''''
n = int(input())
for _ in range(n):
    dp = [[1, 0, 0], [1, 1, 0], [1, 1, 1]]
    a = int(input())
    if a<=3:
        print(sum(dp[a-1]))
        continue
    for i in range(3, a+1):
        tmp = []
        tmp.append(dp[i-1][0])
        tmp.append(dp[i-2][0] + dp[i-2][1])
        tmp.append(dp[i-3][2] + dp[i-3][1] + dp[i-3][0])

        dp.append(tmp)
        print(dp)
    print(sum(dp[a-1]))
'''
# ================================================

from sys import stdin


if __name__ == '__main__':
    t = int(stdin.readline())
    dp = [1] * 10001

    for i in range(2, 10001):
        dp[i] += dp[i - 2]

    for i in range(3, 10001):
        dp[i] += dp[i - 3]


    for _ in range(t):
        n = int(stdin.readline())
        print(dp[n])


