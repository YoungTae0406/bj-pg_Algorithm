import sys
from collections import defaultdict

while True:
    b = defaultdict()
    for i in range(26):
        b[chr(97+i)] = 0
    n = sys.stdin.readline().rstrip()
    n = n.replace(" ", "")
    if n == "*":
        break
    for i in n:
        b[i] += 1
    flag = True
    for i in range(26):
        if b[chr(97+i)] <= 0:
            flag = False
    if flag:
        print("Y")
    else:
        print("N")