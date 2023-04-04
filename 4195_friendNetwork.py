import sys
from collections import defaultdict
test_case = int(input())

# 입력받을때 두명에게 각각 몇명이 연결되어 있는지를 알아야함
# 각 node의 rootnode에 총 몇개가 연결돼있는지에 대한 정보를 기입

while test_case:
    node_root = defaultdict(str)
    node_count = defaultdict(int)

    def find(x):
        if x != node_root[x]:
            node_root[x] = find(node_root[x])
        return node_root[x]

    def union(a, b):
        roota = find(a)
        rootb = find(b)

        if roota != rootb:
            node_root[rootb] = roota
            node_count[roota] += node_count[rootb]
            node_count[rootb] = 1
    def getCount(a, b):
        roota = find(a)
        rootb = find(b)
        if roota == rootb:
            return node_count[roota]
        return node_count[roota] + node_count[rootb]


    friend = int(sys.stdin.readline().strip())
    for _ in range(friend):
        a, b = map(str, sys.stdin.readline().split())
        if a not in node_root:
            node_root[a] = a
            node_count[a] = 1
        if b not in node_root:
            node_root[b] = b
            node_count[b] = 1
        ans = getCount(a, b)
        print(ans)
        #print(node_count)
        union(a, b)


    #print(node_root)
    #print(node_count)
    test_case -= 1





