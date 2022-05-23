stair_num = int(input())
score = [0]+[int(input()) for _ in range(stair_num)]

dp = [0] * (stair_num + 1)
if stair_num == 1:
    dp[1] = score[1]
    print(dp[1])
if stair_num == 2:
    dp[2] = score[1] + score[2]
    print(dp[2])
if stair_num >= 3:
    dp[1] = score[1]
    dp[2] = score[1] + score[2]
    for i in range(3, len(dp)):
        dp[i] = max(dp[i-2] + score[i], dp[i-3] + score[i]+ score[i-1])
    print(dp[stair_num])


