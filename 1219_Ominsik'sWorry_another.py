def check(E):
    visit = [0] * N
    stack = [E]
    while stack:
        a = stack.pop()
        if a == End:
            return True
        visit[a] = 1
        for b, c in network[a]:
            if visit[b] == 0:
                stack.append(b)
    return False

def BF():
    for i in range(N+1):
        if dist[End] == -float('inf') and i == N:
            print('gg')
            return
        for j in range(N):
            if dist[j] == -float('inf'):
                continue
            for E, T in network[j]:
                if dist[j] + T > dist[E]:
                    dist[E] = dist[j] + T
                    #print(i, j, dist)
                    if i == N:
                        if check(E):
                            print('Gee')
                            return False
    return True

N, Start, End, M = map(int, input().split())
dist = [-float('inf')] * N
network = [[] for i in range(N)]

for i in range(M):
    S, E, T = map(int, input().split())
    network[S].append([E, T])
salary = list(map(int, input().split()))
dist[Start] = salary[Start]
#print(network)

for i in range(len(salary)):
    for j in range(len(network[i])):
        for k in range(len(salary)):
            if network[i][j][0] == k:
                network[i][j][1] = salary[k] - network[i][j][1]
#print(network)


if BF():
    print(dist[End])

