from collections import defaultdict
n = int(input())
hu1, hu2 = map(int, input().split())
m = int(input())

graph = defaultdict(list)
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

cnt = 0
visited = [0] * (n+1)
#print(graph)
def dfs(start):
    stack = []
    stack.append(start)
    #visited[start] += 0
    while stack:
        temp = stack.pop()
        if temp == hu2:
            print(visited[temp])
            break
        #visited[temp] = 1
        for k in graph[temp]:
            if visited[k] == 0:
                stack.append(k)
                visited[k] = visited[temp] + 1


dfs(hu1)
#print(visited)
if visited[hu2] == 0:
    print(-1)