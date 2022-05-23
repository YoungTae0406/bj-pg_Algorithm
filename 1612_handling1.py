n = int(input())
temp = 1
ans = 1

if n % 2 == 0 or n % 5 == 0:
    print(-1)
    exit()

while temp % n != 0:
    temp = (temp % n) * 10 + 1
    ans += 1

print(ans)
