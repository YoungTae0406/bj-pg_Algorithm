import sys
cityNum, start, end, transportationNum = map(int, input().split())
edges = []


for _ in range(transportationNum):
    edges.append(list(map(int, sys.stdin.readline().split())))

earnMoney = list(map(int, input().split()))

minusINF = -int(1e9)
dist = [minusINF] * cityNum


def bellman_Ford(start):
    dist[start] = 0
    for i in range(cityNum):
        for j in range(len(edges)):
            stNode = edges[j][0]
            enNode = edges[j][1]
            cost = -edges[j][2]
            #print(i, j, stNode, enNode)
            if stNode == enNode:
                dist[stNode] += earnMoney[stNode]

            if dist[stNode] != minusINF and dist[enNode] < dist[stNode] + cost + \
                    earnMoney[enNode]:
                print(i, stNode, enNode, dist)
                #print(i, stNode, enNode, dist)
                print()
                if i == cityNum-1:
                    return True
                dist[enNode] = dist[stNode] + cost + earnMoney[enNode]

    return False

negative_cycle = bellman_Ford(start)
print(dist)

if dist[end] == minusINF:
    print('gg')
    exit()
if negative_cycle:
    print('Gee')
else:
    print(dist[end])



