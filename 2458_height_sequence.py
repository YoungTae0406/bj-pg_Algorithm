#floyd warshall problem
import sys
stu_num, compare_num = map(int, sys.stdin.readline().split())
adj = [[0 for i in range(stu_num)] for j in range(stu_num)]

# relation check
for i in range(compare_num):
    p, c = map(int, sys.stdin.readline().split())
    adj[p-1][c-1] = 1

# floyd warshall algorithm
for i in range(stu_num):
    for row in range(stu_num):
        for col in range(stu_num):
            if adj[row][i] + adj[i][col] == 2:
                adj[row][col] = 1

cnt = [0 for i in range(stu_num)]
for i in range(stu_num):
    for j in range(stu_num):
        if adj[i][j] == 1:
            cnt[i] += 1
            cnt[j] += 1

print(cnt.count(stu_num-1))


