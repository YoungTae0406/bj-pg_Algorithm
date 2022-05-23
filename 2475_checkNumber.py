#https://www.acmicpc.net/problem/2475

def checkNumber(input_number):
    answer = 0
    for i in input_number:
        a = i*i
        answer += a
    answer = answer%10
    return answer

input_number = list(map(int, input().split()))
print(checkNumber(input_number))