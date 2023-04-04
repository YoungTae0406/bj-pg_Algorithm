''''
import sys
from collections import defaultdict
n = int(input())
numCard = list(map(int, sys.stdin.readline().split()))
m = int(input())
match = list(map(int, sys.stdin.readline().split()))

tempnumCard = list(set(numCard))
tempnumCard.sort()
# 정렬 nlogn하고 이분 탐색하기
ans = defaultdict(int)
#print(numCard)

for i in match:
    left = 0
    right = len(tempnumCard)-1
    mid = (left + right) // 2
    while left <= right:
        #print(left, right, mid, i)
        if tempnumCard[mid] == i:
            ans[i] += 1
            #print(i)
            break
        elif tempnumCard[mid] > i:
            right = mid - 1
            mid = (left + right) // 2
        elif tempnumCard[mid] < i:
            left = mid + 1
            mid = (left + right) // 2
'''

# hashing
from sys import stdin
_ = stdin.readline()
N = map(int,stdin.readline().split())
_ = stdin.readline()
M = map(int,stdin.readline().split())
hashmap = {}
for n in N:
    if n in hashmap:
        hashmap[n] += 1
    else:
        hashmap[n] = 1

print(' '.join(str(hashmap[m]) if m in hashmap else '0' for m in M))
#print(' '.join(str(hashmap[m]) if m in hashmap else '0' for m in M))

'''
from sys import stdin
from collections import Counter
_ = stdin.readline()
N = stdin.readline().split()
_ = stdin.readline()
M = stdin.readline().split()

C = Counter(N)
print(' '.join(f'{C[m]}' if m in C else '0' for m in M))
'''
