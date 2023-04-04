import sys
n, m, k = map(int, input().split())
# Binary Indexed Tree
# 2진법 인덱스 구조를 활용해 구간 합 문제를 효과적으로 해결해 줄 수 있는 자료구조
# 0이 아닌 마지막 비트를 찾는 방법 : K & -k

tree = [0 for _ in range(n+1)]
# tree에는 인덱스가 만약 8이라면 8 & -8은 8(저장되는 개수)이다.
# 그래서 1부터 8까지의 합을 저장해놓는다 인덱스가 3이라면 3 & -3은 1이다. 그래서
# 저장되는 개수가 1개가 된다.
arr = [0 for _ in range(n+1)]

def prefix_sum(i): # i번째까지의 합을 구함
    re = 0
    while i > 0:
        re += tree[i]
        i -= (i & -i)
    return re

def interval_sum(start, end):
    return prefix_sum(end) - prefix_sum(start - 1)

def update(i, c): # 수가 변경될 때 tree에 저장된 누적합들을 변경
    while i <= n:
        tree[i] += c
        i += (i & -i)


for i in range(1, n+1):
    x = int(input())
    arr[i] = x
    update(i, x)

term = m+k
for _ in range(term):
    a, b, c = map(int, sys.stdin.readline().split())
    if a == 1:
        update(b, c - arr[b])
        arr[b] = c
    else:
        print(interval_sum(b, c))
