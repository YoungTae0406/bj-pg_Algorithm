import sys
sys.setrecursionlimit(100000)
n = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
question_list = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]

dp = [[-1] * n for _ in range(n)]


def sol(i ,j):
    if i==j:
        return 1
    elif i+1==j:
        if num_list[i] == num_list[j]:
            return 1
        else:
            return 0
    if dp[i][j] != -1: #memoization
        return dp[i][j]
    if num_list[i] != num_list[j]:
        dp[i][j] = 0
    else:
        dp[i][j] = sol(i+1, j-1)
    return dp[i][j]

for i, j in question_list:
    print(sol(i-1, j-1))


#print(dp)