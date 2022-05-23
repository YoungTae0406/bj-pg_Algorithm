#https://www.acmicpc.net/problem/4963
def bfs(x):
    queue = [x]
    while queue:
        temp_x , temp_y = queue.pop(0)
        maps[temp_x][temp_y] = 0 #current_node visit check
        for a in range(8):
            go_x = di[a]
            go_y = dj[a]
            if 0 <= temp_x+go_x <h and 0 <= temp_y+go_y < w:
                if maps[temp_x+go_x][temp_y+go_y] == 1:
                    maps[temp_x+go_x][temp_y+go_y] = 0 #next_node visit check so, no overlap node
                    queue.append([temp_x+go_x, temp_y+go_y])

di = [-1, -1, -1, 0, 0, 1, 1, 1]
dj = [-1, 0, 1, -1, 1, -1, 0, 1]
while(True):
    count = 0
    w, h= map(int, input().split())
    if w==0 and h==0:
        break
    maps = [list(map(int, input().split())) for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if maps[i][j]:
                count+=1
                bfs([i,j])
    print(count)
