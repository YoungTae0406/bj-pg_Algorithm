n = int(input())
a = list(map(int, input().split()))

dp = [0] * (n)
for i in range(n):
    if i == 0:
        dp[i] = a[i]
        continue
    for j in range(i):
        if a[i] > a[j]:
            dp[i] = max(dp[i], dp[j] + a[i])
        else:
            dp[i] = max(dp[i], a[i])


#print(dp)
print(max(dp))
