'''''
n = int(input())
m = int(input())
broken = list(map(int, input().split()))
available = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
now = 100
ans2 = n-now

for temp in broken:
    available.remove(temp)
ans = 0
ans_button = []
ans_ = []
strn = str(n)

for i in range(len(strn)):
    mx = 100
    for j in available:
        strj = str(j)
        if strn[i] == strj:
            ans_button.append((0, j))
            break
        if strn[i] != strj:
            tempa = int(strn[i])
            tempb = int(strj)
            ab = abs(tempa - tempb)
        ans_button.append((ab, j))
    ans_button.sort()
    ans_.append(ans_button[0])
    ans_button.clear()
    #ans_button.append(mx)
ans += len(ans_)
bb = ""
for ab, j in ans_:
    bb += str(j)
print(bb)

ans += abs(int(bb)-n)
if ans > ans2:
    print(ans2)
else:
    print(ans)
'''

n = int(input())
m = int(input())
broken = list(map(int, input().split()))
mm = abs(n-100)

for i in range(1000001):
    stri = str(i)
    for j in range(len(stri)):
        if int(stri[j]) in broken:
            break
        elif j == len(stri)-1:
            mm = min(mm, abs(n - int(stri)) + len(stri))

print(mm)
