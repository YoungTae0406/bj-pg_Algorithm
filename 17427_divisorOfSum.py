from collections import deque

'''''
def sol(n): #n^2 time complexity
    all = deque(range(2, n+1))
    sum = 1
    while all:
        temp = all.popleft()
        if dp[temp] != 0:
           sum += dp[temp]
           continue
        else:
            for i in range(1, temp+1):
                if temp%i == 0:
                    dp[temp] += i
        sum += dp[temp]
    return sum


n = int(input())
dp = [0] * 1000001
dp[1] = 1
if n==1:
    print(1)
else:
    dp[1] = 1
    print(sol(n))
'''

'''''
time coplexity : n root n
n = int(input())
sum_ = 0
for i in range(1, n + 1):
    for j in range(1, int(i ** 0.5) + 1):
        if i % j == 0:
            sum_ += j
            if i // j != j:  
                sum_ += (i // j)
print(sum_)
'''

# time complexity : n
n = int(input())
sum_ = 0
for i in range(1, n + 1):
    sum_ += (n // i) * i

print(sum_)