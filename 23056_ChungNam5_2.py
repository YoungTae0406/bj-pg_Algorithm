import sys
n, m = map(int, input().split())
ans = []
b = []
while True:
    sclass = tuple(map(str, sys.stdin.readline().split()))
    if sclass[0] == "0" and sclass[1] == "0":
        break
    ans.append(sclass)

#print(ans)
temp = []
sunchak = [0] * (n+1)

for classnum, name in ans:
    if int(classnum) % 2 == 1 and sunchak[int(classnum)] < m:
        sunchak[int(classnum)] += 1
        temp.append((classnum, name))
temp.sort(key=lambda x: (int(x[0]), len(x[1]), x[1]))

for rmclassnum, rmname in temp:
    print(rmclassnum, rmname)
    #ans.remove((rmclassnum, rmname))
temp.clear()

for classnum, name in ans:
    if int(classnum) % 2 == 0 and sunchak[int(classnum)] < m:
        sunchak[int(classnum)] += 1
        temp.append((classnum, name))

temp.sort(key=lambda x: (int(x[0]), len(x[1]), x[1]))
for rmclassnum, rmname in temp:
    print(rmclassnum, rmname)
#print(ans)