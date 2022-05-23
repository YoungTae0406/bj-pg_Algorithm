import sys
n, m = list(map(int, sys.stdin.readline().split()))
card = list(map(int, sys.stdin.readline().split()))
card.sort()

for _ in range(m):
    temp = card[0] + card[1]
    card[0] = temp
    card[1] = temp
    card.sort()

sum = 0
for i in card:
    sum += i
print(sum)