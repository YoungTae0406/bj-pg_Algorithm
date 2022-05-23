a = int(input())
b = a
for i in range(1, a+1):
    print(' '*(b-i)+'*'*(2*i-1))
for j in range(1, a):
    print(' '*j+'*'*(2*(b-j)-1))
