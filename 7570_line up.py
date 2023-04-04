''''
print(init_line)
criteria = child_num // 2
ans_line = deque(range(1, child_num+1))

while init_line != ans_line:
    for i in range(child_num - 1):
        if init_line[i] > init_line[i+1]:
            if init_line[i] > criteria:
                temp = init_line[i]
                init_line.remove(temp)
                init_line.append(temp)
            else:
                temp = init_line[i+1]
                init_line.remove(temp)
                init_line.appendleft(temp)
        else:
            continue
        print(init_line)
        break
'''
import sys
child_num = int(input())
init_line = [0] + list(map(int, sys.stdin.readline().split()))
position = [0 for _ in range(child_num+1)]

if child_num == 1:
    print(0)
    exit()

for i in range(1, len(init_line)):
    position[init_line[i]] = i

cnt = 1
max = -1
for i in range (1, len(init_line) - 1):
    if position[i] < position[i+1]:
        cnt += 1
        if cnt > max:
            max = cnt

    else:
        cnt = 1
#print(position)
print(child_num - max)







