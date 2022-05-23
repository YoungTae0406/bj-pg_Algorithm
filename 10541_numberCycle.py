import sys
sys.setrecursionlimit(10**6)
test_case = int(input())


def make_graph(graph, number):
    ran = len(graph)
    #a = list(range(1, ran))
    for i in range(1, ran):
        graph[i].append(number[i-1])
    return graph

def dfs(graph, start):
    global flag
    visited[start] = True
    for k in graph[start]:
        if not visited[k]:
            dfs(graph, k)
        elif visited[k] == True and finished[start] == False:
            flag = True
    finished[start] = True


for _ in range(test_case):
    n = int(sys.stdin.readline())
    graph = [[] for _ in range(n+1)]
    num = list(map(int, sys.stdin.readline().split()))
    graph = make_graph(graph, num)
    #print(graph)
    sum = 0
    visited = [False] * (n+1)
    finished = [False] * (n+1)
    flag = False
    for i in range(1, n+1):
        if not visited[i]:
            dfs(graph, i)
            if flag:
                sum += 1
    print(sum)