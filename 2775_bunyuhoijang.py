def sol():
    arr = []
    arr.append([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])
    for i in range(1, 15):
        temp = []
        for k in range(1, 15):
            a = 0
            for j in range(k):
                a += arr[i-1][j]
            temp.append(a)
        arr.append(temp)
    return arr


arr = sol()
test_case = int(input())
while test_case:
    n = int(input())
    k = int(input())
    print(arr[n][k-1])
    test_case -= 1

