import sys
n, k = map(int, input().split())
coin = []
for _ in range(n):
    coin.append(int(sys.stdin.readline()))
coin.reverse()
ans = 0
for p in coin:
    if k//p ==0:
        continue
    else:
        temp = k//p
        ans += temp
        k = k - p * temp
    if k == 0:
        break
print(ans)
