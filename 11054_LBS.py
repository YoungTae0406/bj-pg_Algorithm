from collections import deque
#Longest Bytonic
n = int(input())
arr = list(map(int, input().split()))

dp_ascend = [1] * n
dp_descend = [1] * n
dp_bitonic = [0] * n
for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp_ascend[i] = max(dp_ascend[i], dp_ascend[j] + 1)

arr.reverse()
#print(arr)
for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp_descend[i] = max(dp_descend[i], dp_descend[j]+1)
#print(dp_descend)
dp_descend.reverse()
#print(dp_descend)

for i in range(n):
    dp_bitonic[i] = dp_ascend[i] + dp_descend[i]

print(max(dp_bitonic)-1)


'''''
turning_point = max(dp_ascend)
for idx, i in enumerate(dp_ascend):
    if i == turning_point:
        turning_point = idx
        break
#print(dp)

for i in range(turning_point, n):
    for j in range(turning_point, i):
        if arr[i] < arr[j]:
            dp_ascend[i] = max(dp_ascend[i], dp_ascend[j] + 1)
            #print(dp[i])

print(turning_point)
print(max(dp_ascend))
'''
