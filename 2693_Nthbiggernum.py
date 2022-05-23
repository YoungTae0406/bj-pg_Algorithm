N = int(input())
array = []
while N:
    temp = list(map(int, input().split()))
    temp = (sorted(temp))
    temp = list(reversed(temp))
    array.append(temp[2])
    N-=1

for i in range(len(array)):
    print(array[i])

