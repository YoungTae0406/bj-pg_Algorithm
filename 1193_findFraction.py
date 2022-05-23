n = int(input())

line = 0
max_num = 0
while n > max_num:
    line += 1
    max_num += line

gap = max_num - n
if line%2 == 0:
    up = line - gap
    down = gap +1
else:
    up = gap +1
    down = line - gap

print(str(up)+"/"+str(down))