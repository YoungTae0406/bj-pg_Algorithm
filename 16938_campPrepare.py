import itertools

n, l, r, x = map(int, input().split())
problem = list(map(int, input().split()))
ans = []
for i in range(2, n+1):
    h = list(itertools.combinations(problem, i))
    for k in h:
        t_sum = sum(k)
        t_max = max(k)
        t_min = min(k)
        if l <= t_sum <= r and t_max - t_min >= x:
            ans.append(k)

print(len(ans))
