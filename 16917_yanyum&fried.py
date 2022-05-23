a, b, c, x, y = map(int, input().split())
ans = 0

if a+b > 2 * c:
    if x >= y:
        m = x-y
        n = x - m
        ans += c * n * 2
        if c*2 < a:
            ans += m * 2 * c
        else:
            ans += a * m

    else:
        m = y-x
        n = y - m
        ans += c * n * 2
        if c*2 < b:
            ans += m * 2 * c
        else:
            ans += b * m


else:
    ans = a * x + b * y

print(ans)
