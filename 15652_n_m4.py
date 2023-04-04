'''''
from itertools import product
n, m = map(int, input().split())
a = list(range(1, n+1))
ans = list(product(a, repeat=m))
temp = []
for i in ans:
    for j in range(m-1):
        if i[j+1] < i[j]:
            temp.append(i)
            break

for i in temp:
    ans.remove(i)
for i in ans:
    print(*i)
'''
# memory over


