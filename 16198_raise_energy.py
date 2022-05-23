n = int(input())
nnn = list(map(int, input().split()))

def sol(x):
    if len(x) == 2:
        return 0
    ans = 0
    for i in range(1, len(x)-1):
        temp = x[i - 1] * x[i + 1]
        b = x[:i] + x[i+1:]
        temp += sol(b)
        if ans < temp:
            ans = temp
    return ans


a = sol(nnn)
print(a)


