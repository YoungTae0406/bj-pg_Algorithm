import copy

n = int(input())
matryosica = list(map(int, input().split()))

matryosica.sort(reverse=True)

visited = [0 for _ in range(n)]
def solve(idx):
    a = matryosica[idx]
    while idx < len(matryosica):
        if a == matryosica[idx]:
            idx += 1
            continue
        #print('index: ', idx, len(matryosica), a, matryosica, visited)
        if a > matryosica[idx] and not visited[idx]:
            a = matryosica[idx]
            visited[idx] = 1
        idx += 1
            #matryosica.remove(matryosica[i])


for i in range(len(visited)):
    if not visited[i]:
        solve(i)


ans = 0
for i in visited:
    if i == 0:
        ans += 1

print(ans)