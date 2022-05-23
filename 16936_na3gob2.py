def sol(arr, idx, ans):
    #print(ans)
    if idx == n-1:
        for i in range(len(arr)):
            if visited[i] == 0:
                if ans[idx-1] // 3 == arr[i] and ans[idx-1]%3==0:
                    ans.append(arr[i])
                    print(*ans)
                    return ans

                if ans[idx-1] * 2 == arr[i]:
                    ans.append(arr[i])
                    print(*ans)
                    return ans

    if idx == 0:
        for i in range(len(arr)):
            if visited[i] == 0:
                ans.append(arr[i])
                visited[i] = 1
                sol(arr, idx+1, ans)
                visited[i] = 0
                ans.pop()

    if idx >= 1:
        for i in range(len(arr)):
            if visited[i] == 0:
                if ans[idx-1] * 2 == arr[i]:
                    ans.append(arr[i])
                    visited[i] = 1
                    sol(arr, idx+1, ans)
                    visited[i] = 0
                    ans.pop()
                if ans[idx - 1] // 3 == arr[i] and ans[idx-1]%3 == 0:
                    ans.append(arr[i])
                    visited[i] = 1
                    sol(arr, idx + 1, ans)
                    visited[i] = 0
                    ans.pop()


n = int(input())
arr = list(map(int, input().split()))
arr.sort()
ans = []
visited = [0] * n
sol(arr, 0, ans)
