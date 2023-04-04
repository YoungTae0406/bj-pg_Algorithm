'''
import math
import sys

ans = math.inf
visited = []
n, k = map(int, input().split())

stack = [(n,0)]
while stack:
    temp, time = stack.pop()
    if temp == k:
        if ans >= time:
            ans = time
            continue

    if temp not in visited:
        if 0 <= temp <= 100000:
            if temp > k:
                dif = temp - k
                stack.append((temp-dif, time+dif))
            else:
                stack.append((temp+1, time+1))
                stack.append((temp-1, time+1))
                stack.append((temp*2, time))
            visited.append(temp)
    #print(stack, ans)

#print(visited)
print(ans)
'''

'''''
# dijkstra
import math
import heapq

n, k = map(int, input().split())
dp = [math.inf] * 100001
heap = []

def dijkstra(n, k):
    if k <= n:
        print(n-k)
        return
    heapq.heappush(heap, [0, n])
    while heap:
        w, n = heapq.heappop(heap)
        for nx in [n+1, n-1, n*2]:
            if 0 <= nx <= 100000:
                if nx == n * 2 and dp[nx] == math.inf:
                    dp[nx] = w
                    heapq.heappush(heap, [w, nx])
                elif dp[nx] == math.inf:
                    dp[nx] = w+1
                    heapq.heappush(heap, [w+1, nx])
    print(dp[k])

'''''

from collections import deque

n, k = map(int, input().split())
q = deque()
q.append(n)
visited = [0] * 100001
visited[n] = 1

while q:
    tempn = q.popleft()
    if tempn == k:
        print(visited[k]-1)
        break

    for i in [tempn * 2 ,tempn+1, tempn-1]:
        if 0 <= i <= 100000 and visited[i] == 0:
            if i == 2 * tempn:
                q.appendleft(i)
                visited[i] = visited[tempn]
            else:
                q.append(i)
                visited[i] = visited[tempn] +1


