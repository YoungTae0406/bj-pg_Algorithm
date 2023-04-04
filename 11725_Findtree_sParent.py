import sys
from collections import defaultdict
n = int(input())
isParent = [1]
visited = [False] * (n+1)
parent = defaultdict(list)
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    tree[a].append(b)
    tree[b].append(a)


while isParent:
    temp = isParent.pop()
    visited[temp] = True
    for k in tree[temp]:
        if visited[k] == False:
            parent[k].append(temp)
            isParent.append(k)

for k in range(2, len(parent)+2):
    print(*parent[k])

