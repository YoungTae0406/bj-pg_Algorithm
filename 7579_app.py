import sys
'''''
sys.setrecursionlimit(100000)
app, needByte = map(int, input().split())
activeAppByte = list(map(int, input().split()))
inactiveAppCost = list(map(int, input().split()))

# 바이트를 확보하기 위한 비활성화의 최소의 비용

for idx, v in enumerate(inactiveAppCost):
    if v==0:
        needByte -= activeAppByte[idx]
        activeAppByte.remove(activeAppByte[idx])
        inactiveAppCost.remove(v)

dp = [0] * (needByte+1) # index: byte, 값: cost
ans = int(1e9)

def recur(curByte, idx, curCost):
    global ans
    if curByte == needByte:
        ans = min(ans, curCost)
        return

    for i in range(idx, len(activeAppByte)):
        if activeAppByte[i] + curByte <= needByte:
            recur(curByte + activeAppByte[i], i, inactiveAppCost[i] + curCost)


recur(0, 0, 0)
print(ans)
'''

app, needByte = map(int, input().split())
activeAppByte = [0] + list(map(int, input().split()))
inactiveAppCost = [0] + list(map(int, input().split()))

# 바이트를 확보하기 위한 비활성화의 최소의 비용
s = sum(inactiveAppCost)
dp = [[0] * (s+1) for _ in range(app+1)] # [i][j] i: i개 앱 j: 비용 // 값 : 바이트
# 바이트가 값이 크니까 더 작은 비용이 인덱스자리를 차지하게 한 것.

result = 100000
for i in range(1, app+1):
    v = activeAppByte[i]
    c = inactiveAppCost[i]
    for j in range(1, s+1):
        if j < c:
            dp[i][j] = dp[i-1][j]
        else: # 같은 비용에서 더 큰 byte를 가지도록 비교
            dp[i][j] = max(dp[i-1][j-c] + v, dp[i-1][j])
        if dp[i][j] >= needByte:
            result = min(result, j) # 더 작은 비용으로 갱신


print(result)



