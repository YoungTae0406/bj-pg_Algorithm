a, b = map(int, input().split())
ans = 0
for i in range(b):
    if a <= 1:
        break
    a -= 2
    ans += 1
print(ans)