a = input()
b = input()

a=" "+a
b=" "+b
dp = [[0] * len(b) for _ in range(len(a))]

for i in range(1, len(a)):
    for j in range(1, len(b)):
        if a[i] == b[j]:
            dp[i][j] = dp[i-1][j-1]+1
            #before two word add
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])


print(dp[len(a)-1][len(b)-1])
