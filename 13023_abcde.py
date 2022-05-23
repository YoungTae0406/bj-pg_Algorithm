import sys
from collections import deque
n, m = map(int, (input().split()))
friend = [[] for _ in range(n)]
visited = [False] * n
flag = False
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    friend[a].append(b)
    friend[b].append(a)

def dfs(start, depth):
    global flag
    visited[start] = True
    if depth >= 4:
        flag = True
        return
    for k in friend[start]:
        if visited[k] == False:
            dfs(k, depth+1)
            visited[k] = False


for i in range(n):
    dfs(i, 0)
    visited[i] = False
    if flag:
        print(1)
        break
else:
    print(0)
