import sys
n = int(input())
h_arr = []
for _ in range(n):
    h_arr.append(int(sys.stdin.readline()))

# stack을 이용해야 함. 왜 그런가 생각해보니 이전의 값을 가지고 현재 데이터를
# 이전의 값과 함께 계산하고 즉각적으로 처리를 필요로 하기 때문.

# 또 다른 방법으로는 분할과 정복을 이용한 방식이다. 그러면 O(nlogn)으로 해결 가능.

def sol(left, right):
    if left == right:
        return h_arr[left]
    mid = (left + right) // 2
    ans = max(sol(left, mid), sol(mid+1, right))
    # 반씩 쪼개나간다. 직사각형이 한 쪽에만 있을 경우

    lo = mid
    hi = mid+1
    temp = min(h_arr[lo], h_arr[hi])
    ans = max(ans, temp*2)
    # 넓은 직사각형이 가운데를 포함하고 있을 경우

    while left < lo or hi < right:
        if hi < right and ((left == lo) or h_arr[lo-1] < h_arr[hi+1]):
            hi += 1
            temp = min(temp, h_arr[hi])
        else:
            lo -= 1
            temp = min(temp, h_arr[lo])

        ans = max(ans, (hi-lo+1) * temp)
    return ans


ans = sol(0, n-1)
print(ans)