'''
n = int(input())
p = list(map(int, input().split()))
p.sort()
temp = 0
ans = []
for k in p:
    temp += k
    ans.append(temp)
print(sum(ans))
'''
