
rg = set(range(1, 10001))
check = [False] * 10002
ans = set()

for i in range(1, 10001):
    a = len(str(i))
    t = str(i)
    sum = 0
    for k in range(a):
        sum += int(t[k])
    sum += i
    ans.add(sum)


ans = set(sorted(ans))
answer = rg - ans
answer = sorted(answer)
for k in answer:
    print(k)

