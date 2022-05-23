#https://www.acmicpc.net/problem/9095

repi = int(input())
list = []
for _ in range(repi):
    list.append(int(input()))
cache = [0, 1, 2, 4]
for i in range(4, 11):
    cache.append(cache[i-1] + cache[i-2] + cache[i-3])

for j in list:
    print(cache[j])