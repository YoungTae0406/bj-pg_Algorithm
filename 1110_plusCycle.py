'''''
N = int(input())
cnt = 0
temp = N

while True:
    a = temp // 10
    b = temp % 10
    c = (a+b) % 10
    N = (b*10)+c

    cnt += 1
    if temp == N:
        break
'''
input_num = int(input())

num = input_num  # num 변수에 input_num을 지정
cnt = 0
while True:
    sum_num = (num // 10) + (num % 10)  # 각 자릿수를 더한수
    new_num = ((num % 10) * 10) + (sum_num % 10)  # 새로 만들어지는 수
    cnt += 1

    if new_num == input_num :
        break
    num = new_num  # num 변수에 last_num을 지정
print(cnt)