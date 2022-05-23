import itertools as it

test_case = int(input())
number = list(map(int, input().split()))
operator = list(map(int, input().split()))
temp = []

for j in range(4):
    for i in range(operator[j]):
        if j == 0:
            temp.append('a')
        elif j==1:
            temp.append('b')
        elif j==2:
            temp.append('c')
        else:
            temp.append('d')
temp = list(it.permutations(temp))
count = 0
answer = []
for k in temp:
    answer_temp = number[0]
    for p in k:
        if p == 'a':
            answer_temp = answer_temp + number[count+1]
            count += 1
        if p == 'b':
            answer_temp = answer_temp - number[count+1]
            count += 1
        if p == 'c':
            answer_temp = answer_temp * number[count+1]
            count += 1
        if p == 'd':
            if answer_temp < 0:
                answer_temp = abs(answer_temp) // number[count+1]
                answer_temp = answer_temp * -1
                count += 1
            else:
                answer_temp = answer_temp // number[count + 1]
                count += 1

    answer.append(answer_temp)
    count = 0

print(max(answer))
print(min(answer))


