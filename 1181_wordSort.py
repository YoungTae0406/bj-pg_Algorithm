import sys
n = int(input())
ans = []
for _ in range(n):
    ans.append(sys.stdin.readline().strip())

word = dict()
for i in range(1, 51):
    word[i] = []

for j in ans:
    a = len(j)
    if j not in word[a]:
        word[a].append(j)


for i in range(1, 51):
    word[i].sort()
    if len(word[i]) == 0:
        continue
    print(*word[i], sep="\n")
