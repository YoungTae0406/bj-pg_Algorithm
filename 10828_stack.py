from collections import deque
import sys

deq = deque()
for i in range(int(sys.stdin.readline())):
    a = list(sys.stdin.readline().split())
    if a[0] == 'push':
        deq.append(a[1])
    elif a[0] == 'pop':
        if len(deq) == 0:
            print(-1)
        else:
            print(deq.pop())
    elif a[0] == 'size':
        print(len(deq))
    elif a[0] == 'empty':
        if len(deq) == 0:
            print(1)
        else:
            print(0)
    elif a[0] == 'top':
        if len(deq) == 0:
            print(-1)
        else:
            print(deq[len(deq)-1])
