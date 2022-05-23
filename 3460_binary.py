def binary(num):
    if num < 2:
        bin.append(num)
        return
    else:
        a = num  // 2
        b = num % 2
        binary(a)
        bin.append(b)


test_case = int(input())
for _ in range(test_case):
    n = int(input())
    bin = []
    count = 0
    binary(n)
    bin = list(reversed(bin))
    for i in bin:
        if i == 1:
            print(count, end = " ")
        count+= 1