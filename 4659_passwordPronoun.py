import re

# 모음 하나를 반드시 포함
# 모음이 3개 혹은 자음이 3개 연속으로 오면 안됨
# 같은 글자가 연속적으로 두번 오면 안되나, ee와 oo는 허용
while True:
    inp = input()
    if inp == 'end':
        break
    one = re.findall('[aeiou]', inp)
    two = re.findall('([aeiou]{3})|([^aeiou]{3})', inp)
    thr = re.findall(r'([a-df-np-z])\1', inp)

    #print(one, two, thr)
    if len(one) != 0 and len(two) == 0 and len(thr) == 0:
        print("<"+inp+">"+" is acceptable.")
    else:
        print("<"+inp+">"+" is not acceptable.")