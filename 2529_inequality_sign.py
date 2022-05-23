n = int(input())
op = input().split()
flag = [False] * 10
mx, mn = "", ""

def possible(i, j, k):
    if k == '<':
        return i < j
    if k == '>':
        return i > j
    return True

def sol(ind, s):
    global mx, mn
    if ind == n+1:
        if not len(mn):
            mn = s
        else:
            mx = s
        return
    for i in range(10):
        if not flag[i]:
            if ind == 0 or possible(s[-1], str(i), op[ind - 1]):
               flag[i] = True
               sol(ind + 1, s + str(i))
               flag[i] = False


sol(0, "")
print(mx)
print(mn)