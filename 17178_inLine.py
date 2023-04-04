from collections import deque
n = int(input())
ticket = []
for _ in range(n):
    temp = list(map(str, input().split()))
    for i in range(len(temp)):
        a = temp[i]
        b = a.split('-')
        if len(b[1]) == 1:
            b[1] = '00' + b[1]
        elif len(b[1]) == 2:
            b[1] = '0' + b[1]
        b = b[0] + '-' + b[1]
        ticket.append(b)
sortedticket = sorted(ticket) # 사전식으로 배열하니 숫자 부분에서 내가 생각한대로
# 정렬이 안됨.
#print(ticket)
#print(sortedticket)

waiting = [] # stack
ans = ''
idx = 0

for j in ticket:
    if j == sortedticket[idx]:
        idx += 1

    else:
        if len(waiting) != 0:
            waiting_last = waiting[-1]
        else:
            waiting.append(j)
            continue

        while sortedticket[idx] == waiting_last:
            waiting.pop()
            idx += 1
            if len(waiting) != 0:
                waiting_last = waiting[-1]
            else:
                break
        waiting.append(j)
#print(waiting)
while waiting:
    waiting_last = waiting[-1]
    if sortedticket[idx] == waiting_last:
        waiting.pop()
        idx += 1
    else:
        waiting.pop()

if idx != len(sortedticket):
    ans = 'BAD'
else:
    ans = 'GOOD'

#print(waiting, idx)
print(ans)