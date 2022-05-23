N = int(input())
list_num = list(map(int,input().split()))
max = list_num[0]
for i in list_num:
    if max <= i:
        max = i
min = list_num[0]
for j in list_num:
    if min >= j:
        min = j
print(min, max)