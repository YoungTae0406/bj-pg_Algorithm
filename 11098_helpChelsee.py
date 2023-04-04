'''n = int(input())

while n:
    p = int(input())
    p_h = {}
    high = 0
    for i in range(p):
        c, name = input().split()
        p_h[c] = name
        #print(c, name, p_h)
        if int(c) >= high:
            high = int(c)
    print(p_h[str(high)])

    n -= 1
'''
# 2857
'''
import re
fbi = []
p = re.compile('FBI')
ans = []

for i in range(5):
    inp = input()
    temp = p.search(inp)
    if temp:
        ans.append(i+1)

if ans:
    print(*ans)
else:
    print("HE GOT AWAY!")
'''
# 1264
import re

while True:
    inp = input()
    if inp == "#":
        break
    inp = inp.lower()
    a = re.findall('[aeiou]', inp)
    print(len(a))

