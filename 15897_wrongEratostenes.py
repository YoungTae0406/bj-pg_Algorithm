n = int(input())
arr = []
ans = n

j = 0
i = 2
while n > i:
    j = (n - 1) // ((n - 1) // i)
    num = 1 + (n - 1) // i
    ans += (j - i + 1) * num
    #print(i, j, num, ans)
    i = j+1


if n != 1:
    ans += 1
print(ans)
