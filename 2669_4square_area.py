one_s = list(map(int, input().split()))
two_s = list(map(int, input().split()))
thr_s = list(map(int, input().split()))
for_s = list(map(int, input().split()))

enti = list()
enti.append(one_s)
enti.append(two_s)
enti.append(thr_s)
enti.append(for_s)
enti.sort()
#print(enti)

visited = [[0] * 101 for _ in range(101)]
for x, y, mx, my in enti:
    for i in range(x, mx):
        for j in range(y, my):
            visited[i][j] = 1

max_x, max_y, min_x, min_y, = 0, 0, 10000, 10000

for minx, miny, maxx, maxy in enti:
    max_x = max(max_x, maxx)
    max_y = max(max_y, maxy)
    min_x = min(min_x, minx)
    min_y = min(min_y, miny)

total = (max_x - min_x) * (max_y - min_y)
sum = 0
for i in range(min_x, max_x):
    for j in range(min_y, max_y):
        if visited[i][j] == 1:
            sum += 1

print(sum)

