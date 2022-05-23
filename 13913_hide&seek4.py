from collections import deque
n, k = map(int, input().split())
visited = [-1] * 100001
move = [0] * 100001

def path(x, k):
    ans= []
    temp = x
    for _ in range(visited[k]+1):
        ans.append(temp)
        temp = move[temp]
    return ans[::-1]

def bfs(n, k):
    q = deque()
    q.append(n)
    visited[n] = 0
    while q:
        temp = q.popleft()
        if temp == k:
            print(visited[temp])
            a = path(temp, k)
            print(*a)
            break
        n1 = temp + 1
        n2 = temp - 1
        n3 = temp * 2

        for m in [n1, n2, n3]:
            if 0 <= m <= 100000 and visited[m] == -1:
                visited[m] = visited[temp] + 1
                q.append(m)
                move[m] = temp

bfs(n, k)
#print(visited)