def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, x, y):
    a = find_parent(parent, x)
    b = find_parent(parent, y)
    if a > b:
        parent[a] = b
    elif a < b:
        parent[b] = a


n = int(input())  # 도시 개수
m = int(input())  # 여행할 도시 개수
parent = [i for i in range(n + 1)]
graph = [list(map(int, input().split())) for _ in range(n)]
route = list(map(int, input().split()))

for j in range(n):
    for k in range(j + 1, n):
        if graph[j][k] == 1:
            union_parent(parent, j + 1, k + 1)
            print(parent)

prnt = find_parent(parent, route[0])


for a in range(len(route)):
    if find_parent(parent, route[a]) != prnt:
        print("NO")
        exit()
print("YES")