import sys
test_case = int(sys.stdin.readline())
floor = []
me = []
floor_human = [[1] * 14 for _ in range(14)]
for i in range(14):
    floor_human[0][i] = i+1
for _ in range(test_case):
    floor.append(int(sys.stdin.readline()))
    me.append(int(sys.stdin.readline()))

sum_temp = 0

for i in range(1, 14):
    for j in range(0, 14):
        sum_temp = 0
        for k in range(0, j+1):
            print(i-1, j, k)
            sum_temp += floor_human[i-1][j]
        floor_human[i][j] = sum_temp

print(floor_human)
#1.1 1 1
#1.2 3 1,2
#1.3 6 1,2,3
#1.4 10 1,2,3,4
#2.1 1 1
#2.2 4 1,3
#2.3 10 1,3,6