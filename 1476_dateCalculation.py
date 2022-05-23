e, s, m = map(int, input().split())

start = [1, 1, 1]
cnt = 1
for i in range(10000):
    if start[0] == e and start[1] == s and start[2]==m:
        print(cnt)
        break
    start[0] += 1
    if start[0] > 15:
        start[0] = 1
    start[1] += 1
    if start[1] > 28:
        start[1] = 1
    start[2] += 1
    if start[2] > 19:
        start[2] = 1
    cnt+=1
