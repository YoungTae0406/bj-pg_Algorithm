import sys
a, b = list(map(int, sys.stdin.readline().split()))

queue = [(a, 1)]
cnt = -1
while queue:
    temp, temp_cnt = queue.pop(0)
    kk = [temp*2, temp*10+1]
    temp_cnt += 1
    for v in kk:
        if v > b:
            continue
        elif v == b:
            cnt = temp_cnt
            break
        else:
            queue.append((v, temp_cnt))

print(cnt)


