n, m = map(int, input().split()) # 집 안 물건 종류개수, 가방 최대 무게
objects =[]
# 배낭1 문제는 물건이 하나였으면 여기는 여러개

dp = [0] * (m+1) # index : 무게, 값 : 만족도

# 개수를 dp에 하나씩 넣게 되면 최악의 경우 : 10000(m) * 100(n) * 10000(k) -> 시간초과
# k가 log로 줄어들게 되네

for _ in range(n):
    v, c, k = map(int, input().split())
    # 물건 무게, 만족도, 물건의 개수
    logk = 1
    while k > 0:
        logk = min(logk, k)
        objects.append((v*logk, c*logk))
        k -= logk
        logk *= 2

#print(objects)
for v, c in objects:
    for i in range(m, v-1, -1):
        dp[i] = max(dp[i], dp[i-v] + c)

print(dp[m])
