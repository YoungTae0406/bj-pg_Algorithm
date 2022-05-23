a = input()
b = input()

a=" "+a
b=" "+b
dp = [[0] * len(b) for _ in range(len(a))]
#print(*dp, sep="\n")

for i in range(1, len(a)):
    for j in range(1, len(b)):
        if a[i] == b[j]:
            dp[i][j] = dp[i-1][j-1]+1
            #before two word add
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

#print(*dp, sep="\n")
print(dp[len(a)-1][len(b)-1])
n = len(a)-1
m = len(b)-1
ans = []
while n > 0 and m > 0:
    if dp[n][m] == dp[n][m-1]:
        m-=1
    elif dp[n][m] == dp[n-1][m]:
        n-=1
    else:
        ans.append(a[n])
        n-=1
        m-=1
ans = ans[::-1]
print(*ans, sep="")
