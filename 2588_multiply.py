a = input()
b = input()

a_reverse = a[::-1]
b_reverse = b[::-1]
answer = []
a_number = len(a)

for x in b_reverse:
    ten_temp = 0
    ans_three = ''
    number = 0
    for y in a_reverse:
        number+=1
        if number == a_number:
            temp = int(x)*int(y)+ten_temp
            ans_three = str(temp) + ans_three
            continue
        temp = int(x)*int(y)+ten_temp
        if temp > 9:
            ten_temp = temp // 10
            temp = temp % 10
        ans_three = str(temp) + ans_three
    answer.append(ans_three)

ans_sum = 0
one = 1
for i in range(len(answer)):
    ans_sum += int(answer[i]) * one
    one *= 10

for i in answer:
    print(int(i))
print(ans_sum)
