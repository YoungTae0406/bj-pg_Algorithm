import sys

n, s = map(int, sys.stdin.readline().split())
numlist = list(map(int, sys.stdin.readline().split()))
ans = 0

def solve(numlist, index, sum):
    global ans
    if index == n:
        if sum == s:
            ans += 1
        return

    solve(numlist, index+1, sum+numlist[index])
    solve(numlist, index+1, sum)

solve(numlist, 0, 0)
if s == 0:
    ans -= 1
print(ans)