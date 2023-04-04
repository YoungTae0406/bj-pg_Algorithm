import sys
from collections import defaultdict
n, m, x = map(int, input().split())
roads = defaultdict(list)

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())


