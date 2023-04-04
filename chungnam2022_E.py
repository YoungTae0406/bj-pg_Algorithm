n = int(input())
sodduk = list(input())

t = n // 2
ans = 0
for i in range(t):
    if sodduk[i] != sodduk[-(i+1)]:
        ans += 1
print(ans)