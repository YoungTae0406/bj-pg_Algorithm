from collections import defaultdict
import sys
n, m = map(int, input().split())
d = defaultdict(int)
ans = []
for i in range(n):
    inp = sys.stdin.readline().strip()
    d[inp] += 1

for j in range(m):
    inp = sys.stdin.readline().strip()
    d[inp] += 1
    if d[inp] == 2:
        ans.append(inp)

ans.sort()
print(len(ans))
print('\n'.join(f'{ans[i]}' for i in range(len(ans))))
#print('\n'.join(ans))

