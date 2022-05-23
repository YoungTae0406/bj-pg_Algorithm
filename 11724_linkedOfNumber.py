import sys
sys.setrecursionlimit(10**6)
n, m = map(int, input().split())
linked = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    linked[a].append(b)
    linked[b].append(a)

visited = [False] * (n+1)

def dfs(start):
    visited[start] = True
    for k in linked[start]:
        if not visited[k]:
            dfs(k)

sum = 0
flag = False
for i in range(1, n+1):
    if visited[i] == False:
        dfs(i)
        sum += 1
print(sum)