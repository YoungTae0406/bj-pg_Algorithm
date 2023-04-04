import sys
from collections import deque
# (r, c)는 1부터 시작
# 봄 자신의 나이만큼 양분을 먹고 나이가 1 증가. 하나의 칸에 여러 개의 나무가
# 있다면 나이가 어린 나무부터 양분을 먹는다. 양분이 부족해 자신의 나이만큼
# 양분을 먹을 수 없는 나무는 양분을 먹지 못하고 즉시 죽음

# 여름 봄에 죽은 나무가 양분으로 변함. 죽은 나무마다 나이를 2로 나눈 값이
# 양분으로 추가되고 소수점 아래는 버린다.

# 가을 나무가 번식. 번식하는 나무는 나이가 5의 배수여야하고 인접한 8개의 칸에
# 나이가 1인 나무가 생김.

# 겨울 로봇이 땅을 돌아다니며 땅에 양분을 추가. 각 칸에 추가되는 양분의 양은
# A[r][c]이고, 입력으로 주어짐.

n, m, k = map(int, input().split())
# 맵 크기, 나무 개수, 년도
A = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]
tree_map = [[5] * n for _ in range(n)]
trees = [[deque() for _ in range(n)] for _ in range(n)]
dead_trees = [[list() for _ in range(n)] for _ in range(n)]
for _ in range(m):
    x, y, z = map(int, sys.stdin.readline().split())
    trees[x-1][y-1].append(z)


def spring_summer():
    for i in range(n):
        for j in range(n):
            len_ = len(trees[i][j])
            for k in range(len_):
                if tree_map[i][j] < trees[i][j][k]:
                    for _ in range(k, len_):
                        dead_trees[i][j].append(trees[i][j].pop())
                    break
                else:
                    tree_map[i][j] -= trees[i][j][k]
                    trees[i][j][k] += 1

    for i in range(n):
        for j in range(n):
            while dead_trees[i][j]:
                tree_map[i][j] += dead_trees[i][j].pop() // 2

def fall_winter():
    for i in range(n):
        for j in range(n):
            for k in range(len(trees[i][j])):
                if trees[i][j][k] % 5 == 0:
                    for l in range(8):
                        nx, ny, = i + dx[l], j + dy[l]

                        if nx < 0 or nx >= n or ny < 0 or ny >= n:
                            continue
                        trees[nx][ny].appendleft(1)

            tree_map[i][j] += A[i][j]


for i in range(k):
    spring_summer()
    fall_winter()

answer = 0
for i in range(n):
    for j in range(n):
        answer += len(trees[i][j])

print(answer)