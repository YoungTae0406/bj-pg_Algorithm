n, m = map(int, input().split())
a = 100 - n
b = 100 - m
c = 100 - (a+b)
d = a*b

q = 0
r = 0
if d >= 100:
    q = d // 100
    r = d % 100
else:
    q = d // 100
    r = d % 100

ans1, ans2 = c + q, r

print(a, b, c, d, q, r)
print(ans1, ans2)