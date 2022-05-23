import sys
sys.setrecursionlimit(1500*1500)
a, b, c = map(int, sys.stdin.readline().split())
check = [[False] * 1501 for _ in range(1501)]
s = a+b+c

def sol(x, y):
    if check[x][y]:
        return
    check[x][y] = True
    a = [x, y, s-x-y]
    for i in range(3):
        for j in range(3):
            if a[i] < a[j]:
                b = [x, y, s-x-y]
                b[i] += a[i]
                b[j] -= a[i]
                sol(b[0], b[1])


if s % 3 != 0:
    print(0)
else:
    sol(a, b)
    if check[s//3][s//3]:
        print(1)
    else:
        print(0)
