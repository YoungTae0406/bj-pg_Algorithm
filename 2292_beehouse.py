import sys
n = int(sys.stdin.readline())
a = 6
li = [1]
temp = 1
while True:
    temp = temp + a
    li.append(temp)
    a = a + 6
    if temp > 1000010000:
        break
for i in li:
    if n <= i:
        print(li.index(i)+1)
        break
