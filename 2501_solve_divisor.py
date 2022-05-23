N, K = map(int, input().split())
divisor = []
temp = N
while temp:

    if N % temp == 0:
        divisor.append(temp)
    temp-=1

divisor = sorted(divisor)
if K > len(divisor):
    print(0)
else:
    print(divisor[K-1])
