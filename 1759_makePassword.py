import itertools
import sys
l, c = map(int, input().split())
arr = sorted(sys.stdin.readline().split())
#print(arr)
alphabet = set()
for i in range(97, 123):
    alphabet.add(chr(i))
aeiou = set('aeiou')
alphabet -= aeiou

ans = list(itertools.combinations(arr, l))
check_aeiou = 0
check_another = 0
real_ans =""
#print(ans)

for k in ans:
    for p in range(len(k)):
        if len(k)-1 > p:
            if k[p] < k[p+1]:
                real_ans += k[p]
            if k[p] in alphabet:
                check_another += 1
            if k[p] in aeiou:
                check_aeiou += 1
        if p == len(k) - 1:
            real_ans += k[p]
            if k[p] in alphabet:
                check_another += 1
            if k[p] in aeiou:
                check_aeiou += 1

    if len(real_ans) == l and check_aeiou >= 1 and check_another >= 2:
        print(real_ans)
    check_another = 0
    check_aeiou = 0
    real_ans=""



