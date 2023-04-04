a = 0x96
b = 0x100
c = 0x20


print(a*b)
temp = 0x00
temp += a*b
temp += c
print(temp)