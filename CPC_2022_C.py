from collections import defaultdict
n = int(input())
worker = defaultdict(int)

for j in range(n*4): # 4 6 4 10
    inp = list(input().split())
    for i in inp:
        if i == '-':
            continue
        else:
            if i not in worker:
                worker[i] = 0
            else:
                rem = j % 4
                if rem == 0:
                    worker[i] += 4
                elif rem == 1:
                    worker[i] += 6
                elif rem == 2:
                    worker[i] += 4
                else:
                    worker[i] += 10

mx = -1000000
mn = 1000000
for i in worker:
    if worker[i] >= mx:
        mx = worker[i]
    if worker[i] <= mn:
        mn = worker[i]

#print(mx, mn)
#print(worker)
if mx - mn <= 12:
    print("Yes")
else:
    print("No")

