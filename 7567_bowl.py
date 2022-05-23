bowl = input()
a = bowl[0]
hei = 10
for i in range(1, len(bowl)):
    if bowl[i-1] == "(":
        if bowl[i] == "(":
            hei += 5
        if bowl[i] == ")":
            hei += 10
    if bowl[i-1] == ")":
        if bowl[i] == ")":
            hei += 5
        if bowl[i] == "(":
            hei += 10

print(hei)