import sys
n = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))
c = [False] *(n*100000+10)

def solve(index, sum):
    if index == n:
        c[sum] = True
        return
    solve(index+1, sum + num_list[index])
    solve(index+1, sum)

solve(0, 0)
i = 1
while True:
    if c[i] == False:
        break
    i += 1
print(i)