#https://www.acmicpc.net/problem/2798
n, m = map(int, input().split())
card = list(map(int, input().split()))
result = []

for i in range(len(card)):
    for j in range(i+1, len(card)):
        for k in range(j+1, len(card)):
            sum = card[i] + card[j] + card[k]
            if sum > m:
                continue
            else:
                result.append(sum)

print(max(result))