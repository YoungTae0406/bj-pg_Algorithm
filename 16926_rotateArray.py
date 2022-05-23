import sys
from collections import deque
n, m, r = map(int, input().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

down = [0, 1]
up = [0, -1]
left = [-1, 0]
right = [1, 0]

ddm = [0, 1, 0, -1]
ddn = [1, 0, -1, 0]
visited = [[0] * m for _ in range(n)]


def bfs(n_start, m_start, r_cnt):
    q = deque()
    q.append((n_start, m_start))
    r_cnt = r_cnt
    visited[n_start][m_start] = 1
    temp_start = arr[n_start][m_start]
    start_cnt = 1
    temp = 0
    while q:
        temp_n, temp_m = q.popleft()
        #print(temp_n, temp_m)
        dn = temp_n + ddn[r_cnt]
        dm = temp_m + ddm[r_cnt]
        #print(dn, dm)
        #temp = arr[temp_n][temp_m]

        if 0 > dn or dn >= n or 0 > dm or dm >= m or visited[dn][dm] == 1:
            r_cnt += 1

            try:
                dn = temp_n + ddn[r_cnt]
                dm = temp_m + ddm[r_cnt]
            except IndexError:
                a=1
            if dn == n_start and dm == m_start:
                d_temp = arr[dn][dm]
                arr[dn][dm] = temp
                temp = d_temp

                if visited[n_start+1][m_start+1]==0:
                    bfs(n_start+1, m_start+1, 0)
                break
            visited[dn][dm] = 1
            q.append((dn, dm))

            d_temp = arr[dn][dm]
            arr[dn][dm] = temp
            temp = d_temp

            continue

        if 0 <= dn < n and 0 <= dm < m:
            if visited[dn][dm] == 0:
                q.append((dn, dm))
                visited[dn][dm] = 1
                d_temp = arr[dn][dm]

                if start_cnt:
                    arr[dn][dm] = temp_start
                    start_cnt -= 1
                    temp = d_temp
                    continue

                arr[dn][dm] = temp
                temp = d_temp


for i in range(r):
    bfs(0, 0, 0)
    visited = [[0] * m for _ in range(n)]
#bfs(1, 1, 0)
#print(visited)
for k in arr:
    print(*k)
