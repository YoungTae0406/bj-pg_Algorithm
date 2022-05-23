import sys
n = int(input())
num = [int(sys.stdin.readline()) for _ in range(n)]
arr = list(range(1, n+1))

ans = []
stack = []
flag = True

idx = 0

for i in range(len(num)):
    #print(stack)
    if len(stack) > 0:
        if num[i] == stack[-1]:
            #print(i, stack)
            stack.pop()
            ans.append("-")
            continue

    for j in range(idx, len(arr)):
        if num[i] != arr[j]:
            stack.append(arr[j])
            ans.append("+")
        if num[i] == arr[j]:
            if num[i] not in stack:
                stack.append(arr[j])
                ans.append("+")
                stack.pop()
                ans.append("-")
                idx = j+1
                break

    #print(idx)
if len(stack) > 0:
    print("NO")
if len(stack) == 0:
    for p in ans:
        print(p)
#print(stack)

#print(ans)

