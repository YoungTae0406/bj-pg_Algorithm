import sys
n, m = map(int, input().split())
node = [[0] * (n+1) for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    node[a][b] = -1
    node[b][a] = 1

s = int(input())
ans = []
for _ in range(s):
    ans.append(list(map(int, sys.stdin.readline().split())))

for k in range(1, n+1):
    for row in range(1, n+1):
        for col in range(1, n+1):
            if node[row][k] + node[k][col] == -2:
                node[row][col] = -1
                node[col][row] = 1


for px, py in ans:
    print(node[px][py])

