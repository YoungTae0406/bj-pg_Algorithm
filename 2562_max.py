number = []
for i in range(9):
    temp_number = int(input())
    number.append(temp_number)

maxnum = max(number)
print(maxnum)
index = 0
j = 1
for i in number:
    if i == maxnum:
        index = j
        break
    j+=1

print(index)

