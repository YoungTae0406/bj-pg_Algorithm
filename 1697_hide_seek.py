n, k = map(int, input().split())

queue = [n]
visited = [0] * 100001
count = 0
temp_queue = []
while queue:
    temp = queue.pop(0)
    v = [temp+1, temp-1, temp*2]
    if temp == k:
        print(count)
        break

    for i in v:
        if 0 <= i <= 100000:
            if visited[i] == 0:
                temp_queue.append(i)
                visited[i] = 1

    if len(queue) == 0:
        queue.extend(temp_queue)
        temp_queue = []
        count+=1
