import sys
from collections import deque, defaultdict
def bfs(start):
    q = deque()
    q.append(start)
    visited[start] = 1
    while q:
        temp = q.popleft()
        for k in connect_edge[temp]:
            if k == temp: #root node
                return False
            if visited[k] == 0:
                visited[k] = visited[temp] * -1
                q.append(k)
            if visited[k] == visited[temp]:
                return False
    return True


test_case = int(input())
while test_case:
    v, e = map(int, input().split())
#visited = [0] * (v+1)
#connect_edge = [list(map(int, input().split())) for _ in range(e)]
    connect_edge = defaultdict(list)
    for k in range(e):
        a, b = map(int, input().split())
        connect_edge[a].append(b)
        connect_edge[b].append(a)
    visited = [0] * (v+1)
    ans = False
    for p in range(1, v+1):
        if visited[p] == 0:
            ans = bfs(p)
            if not ans:
                print("NO")
                break
    else:
        print("YES")

    test_case -= 1