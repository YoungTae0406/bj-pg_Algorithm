#idx is 1 dimension array number
#c is odd or even
def dfs(idx, c, cnt):
    if chess_size*chess_size-idx+1+cnt <= ans[c] or idx >= chess_size*chess_size:
        return

    ans[c] = max(ans[c], cnt) #cnt = current ans
    x, y = idx//chess_size, idx%chess_size
    j = y
    for i in range(x, chess_size):
        while j < chess_size:
            v = i*chess_size + j
            if not visited[v] and chess[i][j] == 1 and check(v):
                visited[v] = True #when do dfs ... one node
                dfs(v, c, cnt+1)
                visited[v] = False
            j+=2
        j = (c+1)%2 if i%2==0 else c

def check(idx):
    c = idx%2
    i, j = idx//chess_size, idx%chess_size

    for d in range(4):
        x, y = i+dx[d], j+dy[d]
        while 0 <= x <chess_size and 0 <= y <chess_size:
            if visited[x*chess_size+y]:
                return False
            x+= dx[d]
            y+= dy[d]
    return True

chess_size = int(input())
chess = [list(map(int, input().split())) for _ in range(chess_size)]
dx = [1, 1, -1, -1]
dy = [1, -1, -1, 1]
visited = [False] * (chess_size**2)
ans = [0, 0] # odd, even

dfs(0, 0, 0)
dfs(1, 1, 0)
print(sum(ans))

