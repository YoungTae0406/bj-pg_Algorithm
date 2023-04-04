import re

s = input()

tag = re.compile('<[a-zA-Z0-9 ]+>|[a-zA-Z0-9 ]')
sts = (tag.findall(s))
#print(sts)

ans = ''
temp = ''
cnt = 1
for st in sts:
    if st[0] == '<':
        ans += temp[::-1]
        ans += st
        temp=''

    elif st[0] == ' ':
        ans += temp[::-1]+' '
        temp = ''
    elif cnt == len(sts):
        temp += st
        ans += temp[::-1]
        temp = ''

    else:
        temp += st
    cnt += 1
ans += temp
print(ans)