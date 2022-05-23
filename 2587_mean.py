#https://www.acmicpc.net/problem/2587
list = []
for _ in range(5):
    list.append(int(input()))

sum = 0
for i in list:
    sum+= i
mean = sum // 5
list = sorted(list)
print(mean)
print(list[2])