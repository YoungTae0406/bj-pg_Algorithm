#https://www.acmicpc.net/problem/5567
from collections import *
class graph:
    def __init__(self):
        self.edge = defaultdict(list)

    def add_edge(self, u, v):
        self.edge[u].append(v)
        self.edge[v].append(u)

#graph ends when graph reaches 2 depth level
def bfs(graph, start):
    visited = []
    queue = [start]
    repi = 0
    if type(start) == int:
        depth_num = start
    else:
        depth_num = len(start)
    while queue:
        if repi == 3:
            break
        temp = queue.pop(0)
        depth_num -= 1
        if temp not in visited:
            visited.append(temp)
            queue.extend(graph.edge[temp])
        if not depth_num:
            depth_num = len(queue)
            repi +=1
    return visited


num = int(input())
repi = int(input())
g = graph()

for _ in range(repi):
    u, v = map(int, input().split())
    g.add_edge(u, v)
visited = bfs(g, 1)
print(len(visited)-1)
