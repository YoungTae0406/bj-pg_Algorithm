import sys
n = int(input())
x = list(map(int, sys.stdin.readline().split()))

answer = {}
for idx, value in enumerate(x):
    strvalue = str(value)
    answer[strvalue] = idx

cnt = 0
a = set(x)
a = list(a)
a.sort()
for i in a:
    answer[str(i)] = cnt
    cnt += 1

ans = []
for i in x:
    stri = str(i)
    m = answer[stri]
    print(m, end=' ')


