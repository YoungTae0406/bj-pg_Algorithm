jinho = input()
n = int(input())
friends = []
ans = 0
for _ in range(n):
    a = input()
    if a == jinho:
        ans += 1

print(ans)