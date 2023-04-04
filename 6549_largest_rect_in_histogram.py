import sys

ans_arr = []


while True:
    test_case = list(map(int, sys.stdin.readline().split()))
    if test_case[0] == 0:
        break
    n = test_case[0]
    h_arr = test_case[1:]


    def sol(left, right):
        if left == right:
            return h_arr[left]
        mid = (left + right) // 2
        ans = max(sol(left, mid), sol(mid + 1, right))
        # 반씩 쪼개나간다. 직사각형이 한 쪽에만 있을 경우

        lo = mid
        hi = mid + 1
        temp = min(h_arr[lo], h_arr[hi])
        ans = max(ans, temp * 2)
        # 가운데를 포함하고 있을 때 가장 작은 너비 2의 계산

        # 넓은 직사각형이 가운데를 포함하고 있을 경우
        while left < lo or hi < right:
            if hi < right and ((left == lo) or h_arr[lo - 1] < h_arr[hi + 1]):
                hi += 1
                temp = min(temp, h_arr[hi])
            else:
                lo -= 1
                temp = min(temp, h_arr[lo])

            ans = max(ans, (hi - lo + 1) * temp)
        return ans

    ans_arr.append(sol(0, n-1))

for ans in ans_arr:
    print(ans)