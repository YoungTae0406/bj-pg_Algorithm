dp = [1] * 1000001
s = [0] * 10000001

for i in range(2, 1000001): # time complexity nlogn
    j = 1
    while i*j <= 1000000:
        dp[i*j] += i
        j += 1

for i in range(1, 1000001):
    s[i] = dp[i] + s[i-1]


test_case = int(input())
ans = []
for _ in range(test_case):
    a = int(input())
    ans.append(s[a])

for i in ans:
    print(i)

