import sys

T = int(input())
for i in range(0, T):
    n = int(sys.stdin.readline())
    arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    arr.sort()
    #print(arr)
    ans = 1
    MAX = arr[0][1]
    for i in range(1, n):
        if MAX > arr[i][1]:
            ans += 1
            MAX = arr[i][1]
    print(ans)