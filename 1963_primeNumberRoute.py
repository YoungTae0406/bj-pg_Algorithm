import sys
from collections import deque

test_case = int(input())
prime = [True] * 10001

def is_prime():
    for i in range(2, 100):
        if prime[i]:
            for j in range(i+i, 10001, i):
                prime[j] = False

is_prime()

def bfs(start, end, cnt):
    q = deque()
    q.append((start, cnt))
    visited = [False] * 10001
    visited[start] = True

    while q:
        num, count = q.popleft()
        strnum = str(num)
        if num == end:
            return count
        for i in range(4):
            for j in range(10):
                a = str(strnum[:i]) + str(j) + str(strnum[i+1:])
                a = int(a)
                if visited[a] == False and a>=1000 and prime[a] == True:
                    q.append((a, count+1))
                    visited[a] = True


while test_case:
    if test_case <= 0:
        break
    s, e = map(int, input().split())
    print(bfs(s, e, 0))
    test_case-=1
