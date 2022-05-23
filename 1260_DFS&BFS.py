from collections import *
#https://www.acmicpc.net/problem/1260
class graph:
    def __init__(self):
        self.edge = defaultdict(list)
    def add_edge(self,u,v):
        self.edge[u].append(v)
        self.edge[v].append(u)

def BFS(graph, start):
    visited = []
    queue = [start]
    while queue:
        temp = queue.pop(0)
        if temp not in visited:
            visited.append(temp)
            edge_temp = graph.edge[temp][:]
            edge_temp.sort()
            queue.extend(edge_temp)
    return visited

def DFS(graph, start):
    visited = []
    stack = [start]
    while stack:
        temp = stack.pop()
        if temp not in visited:
            visited.append(temp)
            edge_temp = graph.edge[temp][:] # when list copys, = is address copy
            # if only value copys, use [:]
            edge_temp.sort(reverse=True)
            for node in edge_temp:
                stack.append(node)

    return visited

node, edges, start_node = map(int, input().split())
g = graph()
for _ in range(edges):
    u, v = map(int, input().split())
    g.add_edge(u, v)
dfs = DFS(g, start_node)
bfs = BFS(g, start_node)
for i in dfs:
    print(i, end=' ')
print()
for i in bfs:
    print(i, end=' ')