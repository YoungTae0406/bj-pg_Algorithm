''''''
h, w, n, m = map(int, input().split())
a = n+1
b = m+1
col_cnt = 0
row_cnt = 0
while h > 0:
    h -= a
    col_cnt += 1
while w > 0:
    w -= b
    row_cnt += 1

print(col_cnt * row_cnt)
''''

a, b, c = -99, -99, -99
while a != 0 and b != 0 and c != 0:
    a, b, c = map(int, input().split())
    mx = max(a, b, c)
    mn = min(a, b, c)
    another = -99999
    if mx == a:
        if mn == b:
            another = c
        if mn == c:
            another = b
    elif mx == b:
        if mn == a:
            another = c
        if mn == c:
            another = a
    else:
        if mn == a:
            another = b
        if mn == b:
            another = c
    if mx < mn + another:
        print("Invalid")
        continue

    if a == b and b == c:
        print('Equilateral')
    if (a == b and b != c) or (a == c and c != b) or (b == c and b != a):
        print('Isosceles')
    if a != b != c:
        print('Scalene')

    a, b, c = map(int, input().split())