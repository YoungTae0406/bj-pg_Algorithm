import sys
from math import log2
from collections import defaultdict
sys.setrecursionlimit(100005)
# 두 도시를 연결하는 경로 상에서 가장 짧은 도로의 길이와 긴 도로의 길이
n = int(input())
tree = defaultdict(list)
logN = int(log2(n))+1
parent = [[[0, float('inf'), 0] for _ in range(logN)] for _ in range(n+1)]
visited = [0] * (n+1)
tree_dep = [0] * (n+1)

for _ in range(n-1):
    a, b, c = map(int, sys.stdin.readline().split())
    tree[a].append((b, c))
    tree[b].append((a, c))


def dfs(root, depth):
    visited[root] = 1
    tree_dep[root] = depth
    for node, road in tree[root]:
        if not visited[node]:
            parent[node][0] = [root, road, road]
            dfs(node, depth+1)

def setParent():
    dfs(1, 0)
    #print(parent)
    for i in range(1, logN):
        for j in range(1, n+1):
            parent[j][i][0] = parent[parent[j][i-1][0]][i-1][0]
            #print(i, j, parent[j][i-1][0], parent[parent[j][i-1][0]][i-1][0])
            parent[j][i][1] = min(parent[parent[j][i-1][0]][i-1][1], parent[j][i-1][1])
            parent[j][i][2] = max(parent[parent[j][i-1][0]][i-1][2], parent[j][i-1][2])

def LCA(a, b):
    if tree_dep[a] > tree_dep[b]: # b를 더 깊게
        a, b = b, a
    shortest = float('inf')
    longest = 0
    for i in range(logN, -1, -1): # 깊이를 같게
        if tree_dep[b] - tree_dep[a] >= 2 ** i:
            shortest = min(shortest, parent[b][i][1])
            longest = max(longest, parent[b][i][2])
            b = parent[b][i][0]
    if a == b:
        print(shortest, longest)
        return
    for i in range(logN-1, -1, -1): # 깊이가 같은 상태에서 포인터로 최소공통조상으로 이동
        if parent[a][i][0] != parent[b][i][0]:
            shortest = min(shortest, parent[a][i][1], parent[b][i][1])
            longest = max(longest, parent[a][i][2], parent[b][i][2])
            a = parent[a][i][0]
            b = parent[b][i][0]
    shortest = min(shortest, parent[a][0][1], parent[b][0][1])
    longest = max(longest, parent[a][0][2], parent[b][0][2])
    print(shortest, longest)
    return

setParent()
#print(tree_dep)
for _ in range(int(input())):
    d, e = map(int, sys.stdin.readline().split())
    LCA(d, e)


