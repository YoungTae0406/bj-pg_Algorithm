N = int(input())
array = list(map(int, input().split()))
answer = []
count = 0
for i in array:
    for j in range(1, i+1):
        if i%j == 0:
            count+= 1
    if count == 2:
        answer.append(i)
    count = 0
print(len(answer))
