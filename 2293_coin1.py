n, k = map(int, input().split())
coin = [int(input()) for i in range(n)]
dp = [0 for i in range(k+1)]
dp[0] = 1
# dp의 인덱스는 가치의 합

for i in coin: # bottom-up
    for j in range(i, k+1):
        if j-i >= 0:
            dp[j] = dp[j] + dp[j-i]
            # j-i(동전)의 합일 때 dp[j](이전의 과정으로 만들어진 값)를 더한다.
            # dp[j-i]의 합을 더하는 이유는 j-i의 가치에서 i만큼의 가치가
            # 더해질 거라고 생각을 하고 들어가서
print(dp[k])


