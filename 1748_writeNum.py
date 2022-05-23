import time

n = int(input())
cnt = 0
for i in range(1, 10):
    if n >= 10**i:
       cnt += (10**i - 10**(i-1)) * (i)
    else:
        k = i-1
        kten = 10**(i-1)
        temp = n - kten + 1
        cnt = cnt + temp*i
        print(int(cnt))
        break
