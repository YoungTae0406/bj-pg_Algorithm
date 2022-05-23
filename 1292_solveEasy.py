'''''
a, b = map(int, input().split())
count = 50
number = 1
num_array = []
answer = 0
while count:
    for i in range(number):
        num_array.append(number)
    number += 1
    count -= 1
for i in range(a-1, b):
    answer += num_array[i]

print(answer)

'''
