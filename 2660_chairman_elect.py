from collections import defaultdict
from collections import deque

def bfs(start):
    visited = [-1] * (n+1)
    q = deque()
    q.append(start)
    visited[start] += 1
    while q:
        temp = q.popleft()
        for i in graph[temp]:
            if visited[i] == -1:
                visited[i] = visited[temp] + 1
                q.append(i)
    #print(visited, start)
    for k in range(1, n+1):
        if visited[k] == -1:
            return 10000000
    else:
        return max(visited)


n = int(input())
graph = defaultdict(list)
while True:
    a, b = map(int, input().split())
    if a == -1 and b == -1:
        break
    graph[a].append(b)
    graph[b].append(a)


score = 100
ans = []
for i in range(1, n+1):
    mx = bfs(i)
    if mx < score:
        score = mx
        ans = [i]
    elif mx == score:
        ans.append(i)

print(score, len(ans))
print(*sorted(ans))


