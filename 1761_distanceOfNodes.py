import sys
from math import log2
from collections import defaultdict
sys.setrecursionlimit(100000)

n = int(input())
logN = int(log2(n)+1)
tree = defaultdict(list)
tree_dep = [0 for _ in range(n+1)]
visited = [0 for _ in range(n+1)]
parent = [[[0, 0] for _ in range(logN)] for _ in range(n+1)]

for _ in range(n-1):
    a, b, dis = map(int, sys.stdin.readline().split())
    tree[a].append((b, dis))
    tree[b].append((a, dis))

def dfs(root, depth):
    visited[root] = 1
    tree_dep[root] = depth
    for node, dis in tree[root]:
        if not visited[node]:
            parent[node][0][0] = root
            parent[node][0][1] = dis
            dfs(node, depth+1)

def setParent():
    dfs(1, 0)
    for i in range(1, logN):
        for j in range(1, n+1):
            parent[j][i][0] = parent[parent[j][i-1][0]][i-1][0]
            parent[j][i][1] = parent[parent[j][i-1][0]][i-1][1] + parent[j][i-1][1]

def LCA(a, b):
    if tree_dep[a] > tree_dep[b]: # b가 더 깊게
        a, b = b, a
    ans = 0
    for i in range(logN, -1, -1):
        if tree_dep[b] - tree_dep[a] >= 2 ** i:
            ans += parent[b][i][1]
            b = parent[b][i][0]
    if a == b:
        print(ans)
        return
    for i in range(logN-1, -1, -1):
        if parent[a][i][0] != parent[b][i][0]:
            ans += parent[a][i][1] + parent[b][i][1]
            a = parent[a][i][0]
            b = parent[b][i][0]
    ans += parent[a][0][1]
    ans += parent[b][0][1]
    print(ans)
    return

setParent()
for _ in range(int(input())):
    d, e = map(int, sys.stdin.readline().split())
    LCA(d, e)


