n = int(input())
cnt = 1

for i in range(n):
    if i == 0 or i == n-1:
        print("*" * n)
        continue
    for j in range(n):
        if j == 0 or j == n-1:
            print("*", end="")
            continue
        if j == cnt or j == n - cnt - 1:
            print("*", end="")
            continue
        print("", end=" ")
    cnt += 1
    print()