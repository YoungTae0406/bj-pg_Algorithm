import sys
from collections import defaultdict

sys.setrecursionlimit(100000)
n = int(input())
edges = [list(map(int, sys.stdin.readline().split())) for _ in range(n-1)]
m = int(input())
solve = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]

tree = defaultdict(list)
for i in range(n):
    tree[i+1] = []

for a, b in edges:
    tree[a].append(b)
    tree[b].append(a)

visited = [0] * (n+1)
dep = [0] * (n+1)
#print(tree)
parent = [[0] * 20 for _ in range(n+1)]


def dfs(root, depth): # parent 테이블 중 2^0번째 부모와 깊이를 정리
    visited[root] = 1
    dep[root] = depth
    for node in tree[root]:
        if visited[node] == 1:
            continue
        parent[node][0] = root
        dfs(node, depth+1)

def set_parent(): # parent 테이블 완성
    dfs(1, 0)
    for i in range(1, 20):
        for j in range(1, n+1):
            parent[j][i] = parent[parent[j][i-1]][i-1]
            # j는 해당노드번호, i는 2^i에 해당하는

def LCA(a, b):
    if dep[a] > dep[b]:
        a, b = b, a
    for i in range(20-1, -1, -1): # a와 b의 깊이가 같아지도록
        if dep[b] - dep[a] >= 2**i:
            b = parent[b][i]

    if a==b:
        return a

    for i in range(20-1, -1, -1): # 올라가면서 공통 조상 찾기
        if parent[a][i] != parent[b][i]: # 위쪽의 공통 조상들은 다 값이 같을 것이다 그러다가 최소 공통조상의 바로 밑에 자식부터는
            # 이 조건이 해당하게 된다. 그래서 return을 할 때 부모를 리턴하는 것이다.
            a = parent[a][i]
            b = parent[b][i]

    #print(a, b)
    return parent[a][0]

set_parent()
#print(parent)
for a, b in solve:
    print(LCA(a, b))
