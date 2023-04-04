import sys
n = int(input())
m = int(input())
node_parent = [0] * (n+1)
for k in range(1, n+1): # 자기 자신을 부모로 세팅
    node_parent[k] = k

def getParent(x):  # x 노드의 부모 찾기
    if node_parent[x] != x:
        node_parent[x] = getParent(node_parent[x])
    return node_parent[x]

def union(a, b):
    roota = getParent(a)
    rootb = getParent(b)
    #print(a, b, roota, rootb)
    if roota == rootb:
        return
    if roota > rootb:
        node_parent[roota] = rootb
    else:
        node_parent[rootb] = roota
    '''''
    if roota!=rootb:
        node_parent[b] = roota
    '''
def find(a, b):
    roota = getParent(a)
    rootb = getParent(b)
    if roota == rootb:
        return True
    return False


for p in range(1, n+1): # 입력에 대해 union
    conn = [0] + list(map(int, sys.stdin.readline().split()))
    for i in range(p+1, n+1):
        if conn[i] == 1:
            union(p, i)
    #print(node_parent)

#print(node_parent)

citytrace = list(map(int, input().split()))
for r_repu in range(len(citytrace) - 1):
    temp_a = citytrace[r_repu]
    temp_b = citytrace[r_repu+1]
    ans = find(temp_a, temp_b)
    #print(temp_a, temp_b, ans)
    if not ans:
        print("NO")
        break
else:
    print("YES")
