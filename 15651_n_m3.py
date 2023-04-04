from itertools import product
n, m = map(int, input().split())
arrn = list(range(1, n+1))

for i in list(product(arrn, repeat=m)):
    print(*i)

