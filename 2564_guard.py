block_row, block_column = map(int, input().split())
store_num = int(input())
store = []

for i in range(store_num):
    store_dir, store_dist = map(int, input().split())
    temp = (store_dir, store_dist)
    store.append(temp)

donggeun = tuple(map(int, input().split()))
minimum_dist = []


if donggeun[0] == 1: #north
    for dir, dist in store:
        if dir == 1:
            temp_mini = abs(donggeun[1] - dist)
            minimum_dist.append(temp_mini)
        if dir == 2:
            a = block_row - donggeun[1] + block_column + (block_row - dist)
            b = donggeun[1] + block_column + dist
            temp_mini = min(a, b)
            minimum_dist.append(temp_mini)
        if dir == 3:
                temp_mini = donggeun[1] + dist
                minimum_dist.append(temp_mini)
        if dir == 4:
                temp_mini = block_row -donggeun[1] + dist
                minimum_dist.append((temp_mini))
if donggeun[0] == 2:
    for dir, dist in store:
            if dir == 1:
                a = donggeun[1] + block_column + dist
                b = block_row - donggeun[1] + block_column + block_row - dist
                temp_mini = min(a, b)
                minimum_dist.append(temp_mini)
            if dir == 2:
                temp_mini = abs(donggeun[1] - dist)
                minimum_dist.append(temp_mini)
            if dir == 3:
                temp_mini = donggeun[1] + (block_column - dist)
                minimum_dist.append(temp_mini)
            if dir == 4:
                temp_mini = block_row - donggeun[1] + block_column - dist
                minimum_dist.append(temp_mini)
if donggeun[0] == 3:
    for dir, dist in store:
            if dir == 1:
                temp_mini = donggeun[1] + dist
                minimum_dist.append(temp_mini)
            if dir == 2:
                temp_mini = block_column - donggeun[1] + dist
                minimum_dist.append(temp_mini)
            if dir == 3:
                temp_mini = abs(donggeun[1] - dist)
                minimum_dist.append(temp_mini)
            if dir == 4:
                a = donggeun[1] + block_row + dist
                b = block_column - donggeun[1] + block_row + block_column - dist
                temp_mini = min(a, b)
                minimum_dist.append(temp_mini)
if donggeun[0] == 4:
    for dir, dist in store:
            if dir == 1:
                temp_mini = donggeun[1] + block_row - dist
                minimum_dist.append(temp_mini)
            if dir == 2:
                temp_mini = block_column - donggeun[1] + block_row - dist
                minimum_dist.append(temp_mini)
            if dir == 3:
                a = donggeun[1] + block_row + dist
                b = block_column - donggeun[1] + block_row + block_column - dist
                temp_mini = min(a, b)
                minimum_dist.append(temp_mini)
            if dir == 4:
                temp_mini = abs(donggeun[1] - dist)
                minimum_dist.append(temp_mini)

sum = 0
for i in minimum_dist:
    sum += i

print(sum)