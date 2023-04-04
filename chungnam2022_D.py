from collections import deque
from collections import Counter
n = int(input())
sodduk = list(input())

for _ in range(n):
    ans = Counter(sodduk)
    if ans['s'] == ans['t']:
        print(''.join(sodduk))
        break
    else:
        sodduk.pop(0)





