import sys
n, m = map(int, input().split())
arr = [0] + list(map(int, sys.stdin.readline().split()))
tree = [0 for _ in range(n+1)]

def prefix_sum(i):
    ans = 0
    while i > 0:
        ans += tree[i]
        i -= (i & -i)
    return ans

def interval_sum(start, end):
    return prefix_sum(end) - prefix_sum(start-1)

def update(i, c):
    while i <= n:
        tree[i] += c
        i += (i & -i)

for i in range(1, n+1):
    update(i, arr[i])
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    print(interval_sum(a, b))
