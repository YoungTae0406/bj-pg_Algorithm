n, m = map(int, (input().split()))
num = [True]*1000001
num[1] = False
for i in range(2, 1001):
    if num[i]:
        for j in range(i+i, 1000001, i):
            num[j] = False

for i in range(n, m+1):
    if num[i]:
        print(i)