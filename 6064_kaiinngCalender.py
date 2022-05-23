'''''
import sys
test_case = int(sys.stdin.readline())
case = []
for _ in range(test_case):
    case.append(list(map(int, sys.stdin.readline().split())))

start = 1
end = 1
cnt = 0
for m, n, x, y in case:
    for i in range(m-1):
        if start == x:
            break
        start += 1
        if end == (n+1):
            end = (end % n) + 1
        end += 1
        cnt += 1

    temp = end
    end += m
    cnt += m
    while temp != end:
        if end > n:
            end = (end % n)
        if end == y:
            cnt += 1
            print(cnt)
            break
        cnt += m
        end += m
    print(cnt)
    start = 1
    end = 1
    cnt = 0
'''

for _ in range(int(input())):
    m, n, x, y = map(int, input().split())
    ans = 1
    while x <= m*n:
        if x % n == y % n:
            print(x)
            ans = 0
            break
        x += m
    if ans:
        print(-1)



