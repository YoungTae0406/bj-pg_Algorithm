n = int(input())
arr = list(map(int, input().split()))

odd = []
even = []
for i in arr:
    if i % 2==0:
        even.append(i)
    else:
        odd.append(i)


needeven = n // 2
needodd = n - needeven

if len(odd) == needodd and len(even) == needeven:
    print(1)
else:
    print(0)
