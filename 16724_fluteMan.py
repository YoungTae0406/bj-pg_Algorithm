import sys
sys.setrecursionlimit(10**8)
n, m = map(int, input().split())
dirmap = [sys.stdin.readline().rstrip() for _ in range(n)]
#print(dirmap)
visited = [[False] * m for _ in range(n)]
finished = [[False] * m for _ in range(n)]
cnt = 0
#cycle, join in the middle of the cycle, not ~~

def dfs(i, j, dir):
    global cnt
    if visited[i][j] and finished[i][j] == False:
        cnt += 1
        #print(i, j, cnt)
        return
    if finished[i][j]:
        finished[i][j] = True
        return

    visited[i][j] = True

    if dir == "D":
        dirtemp = dirmap[i+1][j]
        #print(dir, i, j)
        dfs(i+1, j, dirtemp)
        finished[i][j] = True

    elif dir == "U":
        dirtemp = dirmap[i-1][j]
        #print(dir, i, j)
        dfs(i-1, j, dirtemp)
        finished[i][j] = True

    elif dir == "R":
        dirtemp = dirmap[i][j+1]
        ##print(dir, i, j)
        dfs(i, j+1, dirtemp)
        finished[i][j] = True

    elif dir == "L":
        dirtemp = dirmap[i][j-1]
        #print(dir, i, j)
        dfs(i, j-1, dirtemp)
        finished[i][j] = True


for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            a = dirmap[i][j]
            dfs(i, j, a)

#print(visited)
#print(finished)
print(cnt)