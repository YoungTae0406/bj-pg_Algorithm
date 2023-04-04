n = int(input())
dp = [0] * (n+1)
dp[0] = 1
if n==1:
    print(1)
elif n==2:
    print(2)
elif n==3:
    print(3)
elif n==4:
    print(4)
else:
    dp[1] = 1
    dp[2] = 2
    dp[3] = 3
    dp[4] = 4
    arr = []
    for i in range(5, n+1):
        for j in range(1, i-3):
            temp = dp[i-(j+2)]*(j+1)
            arr.append(temp)

        temp = max(arr)
        dp[i] = max(dp[i-1]+1, temp)
        # 화면에 그냥 A를 출력하는 경우와 반복문을 통해 2,3,4 버튼을 누른 경우중
        # 최대를 구해 dp에 넣는 과정
        # 최대 최소라면 어떤 경우가 그 후보가 될 수 있을 지를 생각
    print(dp[n])
