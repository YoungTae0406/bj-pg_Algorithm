import sys
n = int(input())
x = []

for i in range(n):
    query = sys.stdin.readline()
    a = query.split()
    #print(a)
    ans = 1
    if a[0] == '1':
        x.append((int(a[1]), int(a[2])))

    if a[0] == '2':
        for one, two in x:
            ans *= one * int(a[1]) + two
        if ans < 0:
            print('-')
        elif ans == 0:
            print(0)
        elif ans > 0:
            print('+')
        #print(ans)


