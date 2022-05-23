import sys
n = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))
operator = list(map(int, sys.stdin.readline().split()))
ans = []
def sol(num_list, index, cur, plus, minus, mul, div):
    if index == n-1:
        ans.append(cur)
        return
    if plus > 0:
        sol(num_list, index+1, cur + num_list[index+1], plus-1, minus, mul, div)
    if minus > 0:
        sol(num_list, index + 1, cur - num_list[index + 1], plus, minus-1, mul, div)
    if mul > 0:
        sol(num_list, index + 1, cur * num_list[index + 1], plus, minus, mul-1, div)
    if div > 0:
        if cur < 0:
            cur = -1 * cur
            cur = cur // num_list[index + 1]
            cur = -1 * cur
            sol(num_list, index+1, cur, plus, minus, mul, div-1)
        else:
            sol(num_list, index + 1, cur // num_list[index + 1], plus, minus, mul, div-1)

sol(num_list, 0, num_list[0], operator[0], operator[1], operator[2], operator[3])
print(max(ans))
print(min(ans))
