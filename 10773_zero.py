import sys

k = int(input())
stack = []
while k:
    temp = int(sys.stdin.readline())
    if temp == 0:
        stack.pop()
    else:
        stack.append(temp)
    k-=1

print(sum(stack))
