n = input()
length = len(n)
start = 10 ** (length - 1)
ans = 0

for i in range(1, int(n)):
    sum = i
    j = str(i)
    for k in range(len(j)):
        sum += int(j[k])
    if sum == int(n):
        ans = i
        print(ans)
        break
if not ans:
    print(0)

