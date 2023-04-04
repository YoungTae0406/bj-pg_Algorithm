import sys
sys.setrecursionlimit(1000000)
n, m = map(int, (input().split()))
a = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]

parent = []
for i in range(n+1):
    parent.append(i)

def find(x): #x의 루트 노드를 찾는 함수
    if x == parent[x]:
        return x

    parent[x] = find(parent[x])
    return parent[x]


def union(x, y): # y를 x에 연결하는 함수
    xroot = find(x) # 각각 루트 노드를 찾아준다
    yroot = find(y)
    if xroot == yroot:
        return
    if xroot < yroot: # 루트 노드가 다르다면
        parent[yroot] = xroot
    else:
        parent[xroot] = yroot


for x, y, z in a:
    if x == 0: # 합집합
        union(y, z)

    else: # 포함되어있는지 확인
        yroot = find(y)
        zroot = find(z)
        if yroot == zroot:
            print("YES")
        else:
            print("NO")


#print(parent)