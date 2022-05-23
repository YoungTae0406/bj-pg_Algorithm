import sys
from collections import deque

n, k = list(map(int, (sys.stdin.readline().split())))
deq = deque([i for i in range(1, n+1)])
ans = []
while len(deq) > 0:
    deq.rotate(-(k-1))
    ans.append(deq.popleft())

print("<", ', '.join(str(i) for i in ans), ">", sep='')
