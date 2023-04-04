import sys

numRoom = int(input())
antEnergy = [0]
for _ in range(numRoom):
    temp = int(sys.stdin.readline())
    antEnergy.append(temp)

parent = [[[0] * 2 for _ in range(numRoom+1)] for _ in range(18)] # [i][j] i는 2^부모 j는 방 번호

for _ in range(numRoom - 1):
    a, b, cm = map(int, sys.stdin.readline().split())
    if b > a:
        parent[0][b][0] = a
        parent[0][b][1] = cm
    else:
        parent[0][a][0] = b
        parent[0][a][1] = cm

# 개미가 올라가는 것은 희소배열을 이용해 log로 빠르게 확인. 방의 개수가 십만이라
# 시간초과가 날 수 있기 때문에. 그리고 희소배열에 부모노드와 부모로 갈때 에너지
# 소모량도 같이 넣는다.

def makeSparseTable():
    for i in range(1, 18):
        for j in range(1, numRoom+1):
            parent[i][j][0] = parent[i-1][parent[i-1][j][0]][0]
            parent[i][j][1] = parent[i-1][parent[i-1][j][0]][1] + parent[i-1][j][1]

makeSparseTable()
#print(parent)

target = 0
for i in range(1, numRoom+1):
    target = i
    for j in range(17, -1, -1):
        if parent[j][target][0] != 0 and parent[j][target][1] <= antEnergy[i]:
            antEnergy[i] -= parent[j][target][1]
            target = parent[j][target][0]
    print(target)
#print(antEnergy)

