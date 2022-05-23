#https://www.acmicpc.net/problem/2606
from collections import defaultdict
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.dic = defaultdict(list)

    def addedge(self, u, v):
        self.dic[u].append(v)
        self.dic[v].append(u)


def bfs(graph, start_node):
    visited = list()
    queue = [start_node]

    while queue:
        n = queue.pop(0)
        if n not in visited:
            visited.append(n)
            queue.extend(graph[n])
    return visited

computer_num = int(input())
repi = int(input())
vertices = [range(1, computer_num+1)]
g = Graph(vertices)

for _ in range(repi):
    u, v = map(int, input().split())
    g.addedge(u, v)

print(len(bfs(g.dic, 1))-1)
