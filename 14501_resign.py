n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
t = []
p = []
for tx, py in a:
    t.append(tx)
    p.append(py)
t.append(0)
p.append(p[len(p)-1])
ans = 0
temp = 0
def recur(time, total):
    global ans
    if time == n:
        ans = max(ans, total)
        return
    if time > n:
        return
    recur(time + 1, total)
    recur(time + t[time], total + p[time])


recur(0, 0)
print(ans)
