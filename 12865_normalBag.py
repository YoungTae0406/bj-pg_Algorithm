'''import sys
n, k = map(int, sys.stdin.readline().split())
wv = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

dp = [0 for _ in range(2*(k+1))]

for temp_w, temp_v in wv:
    dp[temp_w] = temp_v
ans = -100

for i in range(0, k+1):
    for j in range(0, i):
        if dp[i] == 0 or dp[j] == 0:
            continue
        if dp[i+j] == 0:
            ans = dp[i] + dp[j]
        if ans > dp[i+j]:
            dp[i+j] = ans

print(dp[k])
#print(dp)
'''

import sys
read = sys.stdin.readline

N, K = map(int, read().split())
cache = [0] * (K+1) # 인덱스 : 무게, 값 : 가치

for _ in range(N):
    w, v = map(int, read().split())
    for j in range(K, w-1, -1):
        cache[j] = max(cache[j], cache[j-w] + v)
        # 기존의 무게j일때 가치와 물건(무게w이고 가치v인)을 넣었을 때의 가치 중 최댓값
        
print(cache[-1])

#
# 거꾸로 접근.

#================================================#

import sys
read = sys.stdin.readline

N, K = map(int, read().split())
cache = {0: 0}

for _ in range(N):
    curr_w, curr_v = map(int, read().split())
    temp = {}
    for w, v in cache.items():
        if curr_w + w <= K and curr_v + v > cache.get(curr_w + w, 0):
            temp[curr_w + w] = curr_v + v
    cache.update(temp)
print(max(cache.values()))