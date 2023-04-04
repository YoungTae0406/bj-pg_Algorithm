import sys
# 3/1 ~ 11/30

n = int(sys.stdin.readline())
flower = []
for _ in range(n):
    temp = list(map(int, sys.stdin.readline().split()))
    flower.append([temp[0] * 100 + temp[1], temp[2] * 100 + temp[3]])

flower.sort(key = lambda x:(x[0], x[1]))

cnt = 0
end = 0
target = 301

while flower:
    if target >= 1201 or target < flower[0][0]:
        break
    for _ in range(len(flower)):
        if target >= flower[0][0]:
            if end <= flower[0][1]:
                end = flower[0][1]
            flower.remove(flower[0])

        else:
            break
    target = end
    cnt += 1

if target < 1201:
    print(0)
else:
    print(cnt)