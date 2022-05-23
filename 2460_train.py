train = []

for _ in range(10):
    a, b = map(int, input().split())
    train.append([a, b])
max = 0
a = train[0][1]
for i in range(1, 10):
    a = a - train[i][0] + train[i][1]
    if a >= max:
        max = a

print(max)