import copy
n = int(input())
trian = []
dp = []

for _ in range(n):
    temp = list(map(int, input().split()))
    trian.append(temp)

dp = copy.deepcopy(trian)

for i in range(len(trian)-1):
    for idx, k in enumerate(dp[i]):
        if idx == 0:
            if k + dp[i+1][0] > dp[i+1][0]:
                dp[i+1][0] = k + dp[i+1][0]
            if k + dp[i+1][1] > dp[i+1][1]:
                dp[i+1][1] = k + dp[i+1][1]
        else:
            if k + trian[i+1][idx] > dp[i+1][idx]:
                #print(trian[i+1][idx])
                dp[i+1][idx] = k + trian[i+1][idx]
            if k + dp[i+1][idx+1] > dp[i+1][idx+1]:
                dp[i+1][idx+1] = k + dp[i+1][idx+1]

i = len(dp) - 1
print(max(dp[i]))

