import sys
n, c = map(int, input().split())
house_x = []
for _ in range(n):
    house_x.append(int(sys.stdin.readline()))
house_x.sort()
ans = 0

def binarySearch(x, c):
    global ans
    low = 1
    end = x[-1] - x[0]

    while low <= end:
        mid = (low + end) // 2
        cur_router = x[0]
        ans_c = 1
        temp = int(10**6)
        for i in range(n):
            if cur_router + mid <= x[i]:
                temp = min(temp, x[i] - cur_router)
                cur_router = x[i]
                ans_c += 1

        if ans_c < c:
            end = mid - 1

        else:
            low = mid + 1
            ans = max(ans, temp)
    return ans

print(binarySearch(house_x, c))
