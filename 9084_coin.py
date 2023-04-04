test_case = int(input())
ans = []
while test_case:
    num_coin = int(input())
    coin = list(map(int, input().split()))
    make_money = int(input())

    dp = [0] * (make_money+1) # 인덱스:금액, 값:방법의 수
    dp[0] = 1

    for i in coin:
        for j in range(i, make_money+1):
            dp[j] = dp[j] + dp[j-i] # 기존의 j금액 동전과 j-i금액 동전의 방법의 수에
            # j-i 금액에서 j 동전을 추가한 방법의 수니까

    #print(dp)
    print(dp[make_money])
    test_case -= 1

#
