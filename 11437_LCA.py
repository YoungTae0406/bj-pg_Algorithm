import sys
from collections import defaultdict

def LCA(a, b):
    global parent
    a_level = level[a]
    b_level = level[b]
    pa = a
    pb = b
    # if a_level < b_level:
    #   a_level, b_level = b_level, a_level
    # while a_level != b_level :
    #   pa = parent[pa]
    # while pa != pb:
    #   pa = parent[pa]
    #   pb = parent[pb]

    if a_level == b_level:
        while pa != pb:
            pa = parent[pa]
            pb = parent[pb]
        print(pa)
        return

    else:
        if a_level > b_level:
            dif = a_level - b_level
            for i in range(dif):
                pa = parent[pa]
            while pa != pb:
                pa = parent[pa]
                pb = parent[pb]
            print(pa)
            return

        else:
            dif = b_level - a_level
            for i in range(dif):
                pb = parent[pb]
            while pa != pb:
                pa = parent[pa]
                pb = parent[pb]
            print(pb)
            return


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

root = 1
level = {}
visited = [0] * (n+1)
level[1] = 1
#print(tree)
parent = {}

def dfs(root):
    stack = [root]
    while stack:
        temp = stack.pop()
        if visited[temp] == 0:
            visited[temp] = 1
            for k in tree[temp]:
                if visited[k] == 1:
                    parent[temp] = k
                    continue
                stack.append(k)
                level[k] = level[temp] + 1


dfs(root)
#print(level)
#print(parent)

for ai, bi in solve:
    LCA(ai, bi)