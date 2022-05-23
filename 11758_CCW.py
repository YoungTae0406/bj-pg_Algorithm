ans = [[]] * 3
figure = 0

def findgrad(dx,dy):
    if dx != 0:
        figure = dy/dx
    else:
        figure = float('inf')
    return figure


for i in range(3):
    ans[i] = list(map(int, input().split()))
S2 = (ans[1][0] - ans[0][0]) * (ans[2][1] - ans[0][1]) - (ans[1][1] - ans[0][1]) * (ans[2][0] - ans[0][0])

if S2 > 0:
    print(1)
elif S2 == 0:
    print(0)
else:
    print(-1)