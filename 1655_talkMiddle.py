import sys
import heapq
n = int(input())
leftheap = []
rightheap = []
ans = []

for _ in range(n):
    temp = int(sys.stdin.readline())
    if len(leftheap) == len(rightheap):
        heapq.heappush(leftheap, (-temp, temp))
    else:
        heapq.heappush(rightheap, (temp, temp))

    if rightheap and leftheap[0][1] > rightheap[0][1]:
        a = heapq.heappop(leftheap)[1]
        b = heapq.heappop(rightheap)[1]
        heapq.heappush(leftheap, (-b, b))
        heapq.heappush(rightheap, (a, a))

    ans.append(leftheap[0][1])
for k in ans:
    print(k)
