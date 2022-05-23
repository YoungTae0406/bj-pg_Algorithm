#https://www.acmicpc.net/problem/15988
repi = int(input())
list = []
for _ in range(repi):
    list.append(int(input()))
cache = []
cache.append(0)
cache.append(1)
cache.append(2)
cache.append(4)
for i in range(4, 1000001):
    cache.append(cache[i-1]%1000000009 + cache[i-2]%1000000009 + cache[i-3]%1000000009)

for j in list:
    print(cache[j]%1000000009)