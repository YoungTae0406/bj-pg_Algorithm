N = int(input())
arr = [[0 for _ in range(101)] for _ in range(101)]

for _ in range(N):
    a, b = map(int, input().split())

    for i in range(a, a+10):
        for j in range(b, b+10):
            arr[i][j] = 1

count = 0
for row in arr:
    count+= row.count(1)
print(count)






