'''''
import sys
from collections import defaultdict, deque

input = sys.stdin.readline
n = int(input())
m = int(input())
info = []
for _ in range(m):
    info.append(list(map(int, input().split())))

info.sort()
a = defaultdict()
for i in range(n):
    a[i+1] = []

for q in range(m):
    big, small = info[q]
    a[big].append((small, 1))
    a[small].append((big, 0))

print(a)

def bfs(key):
    que = deque()
    que.append(key)
    visited = []
    seet = set()
    flag = -1
    cnt = 1
    while que:
        temp = que.popleft()
        for v in a[temp]:
            kk, fl = v
            seet.add(fl)
        seet = list(seet)
        print(seet)
        if len(seet) == 2:
            for ii in range(len(a[temp])):
                que.append(a[temp][ii][0])
                cnt += 1
        if len(seet) == 1:
            print(2)
            if seet in [1]:
                flag = 1
                for ii in range(len(a[temp])):
                    if a[temp][ii][1] == flag:
                        que.append(a[temp][ii][0])
                        cnt += 1
            if seet in [0]:
                flag = 0
                for ii in range(len(a[temp])):
                    if a[temp][ii][1] == flag:
                        que.append(a[temp][ii][0])
                        cnt += 1
        seet = set(seet)
    return cnt

for s in range(1, n+1):
    print(n - bfs(s))
'''

import sys
input = sys.stdin.readline
inf = 10**5

n = int(input())
m = int(input())
dp = [[inf] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        if i==j:
            dp[i][j] = 0

for i in range(m):
    a, b = map(int, input().split())
    dp[a][b] = 1

for k in range(1, n+1): # node k
    for a in range(1, n+1): # start a
        for b in range(1, n+1):
            dp[a][b] = min(dp[a][b], dp[a][k] + dp[k][b])

#print(*dp, sep="\n")
for a in range(1, n+1):
    count = 0
    for b in range(1, n+1):
        if dp[a][b] == inf and dp[b][a] == inf:
            count += 1
    print(count)
