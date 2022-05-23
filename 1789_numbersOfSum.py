def sum(num):
    return num * (num+1) // 2

S = int(input())
i = 1
answer = 0
while True:
    a = sum(i)
    b = sum(i+1)
    if a <= S < b :
        answer = i
        break
    else:
        i+=1
print(answer)