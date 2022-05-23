import sys
sys.setrecursionlimit(10**5)
num_subway = int(sys.stdin.readline())
conn = [[i] for i in range(0, num_subway+1)]
for _ in range(num_subway):
    a, b = map(int, sys.stdin.readline().split())
    conn[a].append(b)
    conn[b].append(a)

visited = [False] * (num_subway+1)
surcle = []

def dfs(x, start, v):
    visited[x] = True
    if x in conn[start] or x == start:
        if v>=3:
            surcle.append(x)
            return
    for i in conn[x]:
        if visited[i] == False:
            dfs(i, start, v+1)
            visited[i] = False

for i in range(1, num_subway+1):
    dfs(i, i, 1)
    visited[i] = False

t = num_subway +1
def mmin(start, v):
    global t
    visited[start] = True
    for i in conn[start]:
        if i in surcle:
            t = min(t, v)
            return
        if visited[i] != True:
            mmin(i, v+1)
            visited[i] = False

brray = []
for i in range(1, num_subway+1):
    if i in surcle:
        brray.append(0)
    else:
        mmin(i, 1)
        brray.append(t)
        t = num_subway+1
        visited[i] = False

print(*brray)
print(surcle)