import sys
n, m, r = map(int, (input().split()))
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
cal = list(map(int, input().split()))

def sol1(array):
    n = len(arr)
    m = len(arr[0])
    for i in range(len(array)//2):
        array[i], array[len(array) -1 -i] = array[len(array) -1 -i], array[i]
    return array

def sol2(array):
    n = len(arr)
    m = len(arr[0])
    for i in range(n):
        for j in range(m//2):
            array[i][j], array[i][m-j-1] = array[i][m-j-1], array[i][j]
    return array

def sol3(array):
    n = len(arr)
    m = len(arr[0])
    temp = []
    for i in range(m):
        tt = []
        for j in range(n-1, -1, -1):
            tt.append(array[j][i])
        temp.append(tt)
    return temp

def sol4(array):
    temp = []
    n = len(arr)
    m = len(arr[0])
    for i in range(m-1, -1, -1):
        tt = []
        for j in range(0, n):
            tt.append(array[j][i])
        temp.append(tt)
    return temp

def sol5(array):
    n = len(arr)
    m = len(arr[0])
    for i in range(n//2):
        for j in range(m//2):
            array[i][j], array[i][j+m//2] = array[i][j+m//2], array[i][j]

    for i in range(m//2):
        for j in range(n//2):
            array[j][i], array[j+n//2][i] = array[j+n//2][i], array[j][i]

    for i in range(n//2, n):
        for j in range(m//2):
            array[i][j], array[i][j+m//2] = array[i][j+m//2], array[i][j]

    return array

def sol6(array):
    n = len(arr)
    m = len(arr[0])
    for i in range(n//2):
        for j in range(m//2):
            array[i][j], array[i][j+m//2] = array[i][j+m//2], array[i][j]
    for i in range(m-1, m//2-1, -1):
        for j in range(n//2):
            array[j][i], array[j+n//2][i] = array[j+n//2][i], array[j][i]
    for i in range(n//2, n):
        for j in range(m//2):
            array[i][j], array[i][j+m//2] = array[i][j+m//2], array[i][j]
    return array

for k in cal:
    if k == 1:
        arr = sol1(arr)
    if k == 2:
        arr = sol2(arr)
    if k == 3:
        arr = sol3(arr)
        #print(arr, arr[0], arr[0][0])
    if k == 4:
        arr = sol4(arr)
    if k == 5:
        arr = sol5(arr)
    if k == 6:
        arr = sol6(arr)
for i in arr:
    print(*i, end="\n")
