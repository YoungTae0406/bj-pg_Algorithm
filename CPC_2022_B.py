n = int(input())

# 푸앙이가 먼저

a = 1
while n > 0:
    if n < a:
        break
    n = n - a
    a += 1

if a % 2 == 1:
    print(a - n)

else:
    print(0)

