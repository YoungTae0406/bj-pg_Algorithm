import sys
from collections import deque
n, m, k = map(int, input().split())
# n is mapsize.    m is tree number    k is year
a = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
tree = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]

first_map = [[5] * (n+1) for _ in range(n+1)]
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

tree.sort(key = lambda x : x[2])
dead_tree = []
temp_tree = []
index = []
for mmm in range(k):
    #print("-----------------",mmm,"--------------------")
    #print(len(tree))
    #print(tree)
    for i in range(len(tree)):
    #spring
        #tree.sort(key=lambda x: x[2])

        try:
            x, y, age = tree[i][0], tree[i][1], tree[i][2]
            #print(x, y, age, i)
            if first_map[x][y] - age >= 0:
                first_map[x][y] -= age
                tree[i][2] += 1
            else:
                dead_tree.append(tree[i])
                index.append(i)

        except IndexError:
            print(x, y, age, i, "error")
        #print(tree)
        #print(*first_map, sep="\n")
    fl = 0
    for nnn in index:
        tree.pop(nnn-fl)
        fl+=1
    index.clear()
    #print(tree)
    #print(*first_map, sep="\n")
#summer
    for j in range(len(dead_tree)):
        deadx, deady, deadage = dead_tree[j][0], dead_tree[j][1], dead_tree[j][2]
        energy = deadage // 2
        first_map[deadx][deady] += energy


#fall
    for i in range(len(tree)):
        x, y, age = tree[i][0], tree[i][1], tree[i][2]
        if age % 5 == 0:
            #print(x, y, age)
            for kk in range(8):
                nx = x + dx[kk]
                ny = y + dy[kk]
                if 1 <= nx < n+1 and 1<= ny < n+1:
                    #print(nx, ny, x, y)
                    tree.append([nx, ny, 1])

#winter
    for i in range(1, n+1):
        for j in range(1, n+1):
            first_map[i][j] += a[i-1][j-1]
    #print(*first_map, sep="\n")
    tree.sort(key=lambda x: x[2])
    #print(tree)

    #print(dead_tree)
    dead_tree.clear()

print(len(tree)
