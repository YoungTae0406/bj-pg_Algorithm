import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

bus_info = [[10**7] * (n+1) for _ in range(n+1)]

for p in range(m):
    a, b, cost = map(int, input().split())
    if bus_info[a][b] != 10**7:
        temp = min(cost, bus_info[a][b])
        bus_info[a][b] = temp
    else:
        bus_info[a][b] = cost

for i in range(1, n+1):
    for j in range(1, n+1):
        if i==j:
            bus_info[i][j] = 0


for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            bus_info[i][j] = min(bus_info[i][j], bus_info[i][k] + bus_info[k][j])

for i in range(1, n+1):
    for j in range(1, n+1):
        if bus_info[i][j] != 10**7:
            print(bus_info[i][j], end = " ")
        else:
            print(0, end=" ")
    print()