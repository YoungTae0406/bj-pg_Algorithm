#11729
import heapq, sys

heap = []
for _ in range(int(sys.stdin.readline())):
    temp = int(sys.stdin.readline()) * -1
    if temp == 0:
        if len(heap) == 0:
            print("0")
        else:
            print(heapq.heappop(heap) * -1)
    else:
        heapq.heappush(heap, temp)
