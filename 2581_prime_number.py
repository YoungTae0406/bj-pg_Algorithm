M = int(input())
N = int(input())

prime = []
count = 0
for i in range(M, N+1):
    for j in range(1, i+1):
        if i%j == 0:
            count += 1
        if count > 2 :
            break
    if count == 2:
        prime.append(j)
    count = 0
sum = 0
for i in prime:
    sum += i

if len(prime) != 0:
    print(sum)
    print(min(prime))
else :
    print(-1)