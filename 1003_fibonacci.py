#https://www.acmicpc.net/problem/1003

def fibonacci(num):
    if num==0:
        num_zero[0] = 1
        num_one[0] = 0
        return (num_zero[0], num_one[0])
    elif num==1:
        num_zero[num] = 0
        num_one[num] = 1
        return (num_zero[1], num_one[1])
    else:
        if num_zero[num] == -1 and num_one[num] == -1:
            temp0, temp1 = fibonacci(num-1)
            temp00, temp11 = fibonacci(num-2)
            temp0 += temp00
            temp1 += temp11
            num_zero[num] = temp0
            num_one[num] = temp1
            return (num_zero[num], num_one[num])
        else:
            return (num_zero[num], num_one[num])

repi = int(input())
list = []
for _ in range(repi):
    list.append(int(input()))
num_zero = [-1 for _ in range(41)]
num_one = [-1 for _ in range(41)]
for i in list:
    a, b = fibonacci(i)
    print(a, b)