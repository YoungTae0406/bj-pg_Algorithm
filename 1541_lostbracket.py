# 최소의 값을 만들어야 하니 - 뒤에 + 가 있다면 + 숫자들을 괄호로 묶기
# - 뒤에 -가 있다면 괄호는 그 전까지 숫자만 묶기
'''
import re

p = str(input())
num = []
operand = []

for i in re.split('[+-]', p):
    if not i:
        continue
    num.append(int(i))

for i in re.split('[^+-]', p):
    if not i:
        continue
    operand.append(i)

print(num, operand)
bracket = []
outeridx = 0
temp = []
for idx, ope in enumerate(operand):
    if len(temp) == 2:
        bracket.append(temp)
        temp = []

    if ope == '-':
        if not temp: # - 연산자가 앞에서 나오지 않았으면
            temp.append(outeridx)
        else: # - 연산자가 앞에서 한 번 나왔으면
            temp.append(outeridx-1)
            bracket.append(temp)
            temp = []
            temp.append(outeridx)
        outeridx += 1
    else:
        if idx == len(operand) - 1: # 반복이 끝나면
            temp.append(outeridx)
        outeridx += 1
        continue

if len(temp) == 2:
    bracket.append(temp)
    temp = []

print(bracket)
sum = 0

ans = ''
for a, b in bracket:
    if a == b:
        continue
    for i in range(len(num) - 1):
        if a+1 == i:
            ans += '('
        ans += str(num[i])
        ans += operand[i]



ans += str(num[len(num)-1])
print(ans)
'''

a = input().split('-')
sum = 0
for i in a[0].split('+'):
    sum += int(i)

for i in a[1:]:
    for j in i.split('+'):
        sum -= int(j)

print(sum)
