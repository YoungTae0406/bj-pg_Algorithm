n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]

visited = [False for _ in range(n)]
min_ = int(1e9)

def choiceTeam(depth, idx):
    global min_
    if depth == n//2:
        stat1 = 0
        stat2 = 0
        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]:
                    stat1 += s[i][j]
                elif not visited[i] and not visited[j]:
                    stat2 += s[i][j]
        min_ = min(abs(stat1 - stat2), min_)
        return

    for i in range(idx, n):
        if visited[i] == False:
            visited[i] = True
            choiceTeam(depth+1, i+1)
            visited[i] = False


choiceTeam(0, 0)
print(min_)
