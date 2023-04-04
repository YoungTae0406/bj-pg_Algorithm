from collections import deque
totalFloor, ghcurrent, startlinkf, up, down = map(int, input().split())

visited = [0 for _ in range(totalFloor+1)]
q = deque()
cnt = 0
q.append((ghcurrent, cnt))
visited[ghcurrent] = 1

while q:
    cur, cur_cnt = q.popleft()
    if cur == startlinkf:
        print(cur_cnt)
        exit()

    upnx = cur + up
    downnx = cur - down

    if 1 <= upnx <= totalFloor:
        if not visited[upnx]:
            q.append((upnx, cur_cnt+1))
            visited[upnx] = 1
    if 1 <= downnx <= totalFloor:
        if not visited[downnx]:
            q.append((downnx, cur_cnt+1))
            visited[downnx] = 1
if len(q) == 0:
    print("use the stairs")


