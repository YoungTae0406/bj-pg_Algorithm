import sys
from collections import defaultdict, deque
n, m = map(int, input().split())

# bfs + 이분탐색
# 무게의 범위가 있으므로 무게를 가지고 이분탐색

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
start, end = map(int, input().split())

def bfs(weight):
    q = deque()
    q.append(start)
    visited = [0 for _ in range(n+1)]
    visited[start] = 1
    while q:
        temp = q.popleft()
        if temp == end:
            return True
        for next, w in graph[temp]:
            if not visited[next] and w >= weight:
                q.append(next)
                visited[next] = 1
    return False


_min, _max = 1, 1000000000
ans = _min
while _min <= _max:
    mid = (_min + _max) // 2
    if bfs(mid):
        ans = mid
        _min = mid + 1
    else:
        _max = mid - 1

print(ans)


