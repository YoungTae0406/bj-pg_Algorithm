from itertools import combinations

n = int(input())
arr = list(map(int, input().split()))

maax = sum(arr)
m = set()
for k in range(1, len(arr)+1):
    for p in combinations(arr, k):
        m.add(sum(p))

print(maax - len(m))
