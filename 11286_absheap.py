import sys, heapq, math

heap = []
n = int(input())
for i in range(n):
    a = int(sys.stdin.readline())
    if a != 0:
        heapq.heappush(heap, (abs(a), a))
    else:
        if not heap:
            print(0)
        else:
            print(heapq.heappop(heap)[1])
