import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
dp = [1] * n
num_dp = [[] for _ in range(n)]
for i in range(n):
    num_dp[i].append(arr[i])
#print(num_dp)

for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            if dp[j]+1 > dp[i]:
                dp[i] = dp[j]+1
                num_dp[i] = num_dp[j] + [arr[i]]
            else:
                dp[i] = dp[i]

print(max(dp))
m = max(dp)
index = 0
for idx, k in enumerate(dp):
    if k == m:
        index = idx
#print(dp)
print(*(num_dp[index]))