import sys
v, e = map(int, input().split())
INF = int(1e9)

edges = []
dist = [0] + [INF] * v
for _ in range(e):
    edges.append(list(map(int, sys.stdin.readline().split())))

def bellman_Ford(start):
    dist[start] = 0
    for i in range(v):
        for j in range(e):
            cur_node = edges[j][0]
            next_node = edges[j][1]
            cost = edges[j][2]

            if dist[cur_node] != INF and dist[next_node] > dist[cur_node] + cost:
                dist[next_node] = dist[cur_node] + cost
                #print(dist, i, j)
                if i == v-1:
                    return True

    return False


negative_cycle = bellman_Ford(1)

if negative_cycle:
    print(-1)
else:
    for i in range(2, v+1):
        if dist[i] == INF:
            print(-1)
        else:
            print(dist[i])