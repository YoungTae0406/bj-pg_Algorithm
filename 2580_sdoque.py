def square(x, y):
    return (x//3) * 3 + (y//3)
def go(z):
    if z == 81:
        for row in a:
            print(' '.join(map(str, row)))
        return True
    x = z // 9
    y = z % 9
    if a[x][y] != 0:
        return go(z+1)
    else:
        for i in range(1, 10):
            if c1[x][i] == False and c2[y][i] == False and c3[square(x,y)][i] == False:
                c1[x][i] = c2[y][i] = c3[square(x, y)][i] = True
                a[x][y] = i
                #print(c2)
                #print(c3)
                if go(z+1):
                    return True
                a[x][y] = 0
                c1[x][i] = c2[y][i] = c3[square(x, y)][i] = False
    return False


a = [list(map(int, input().split())) for _ in range(9)]
c1 = [[False] * 10 for _ in range(9)]
c2 = [[False] * 10 for _ in range(9)]
c3 = [[False] * 10 for _ in range(9)]
for i in range(9):
    for j in range(9):
        if a[i][j]:
            c1[i][a[i][j]] = True # c1[i][j] : i row has j number -> true
            c2[j][a[i][j]] = True # c2[i][j] : i col has j number -> true
            c3[square(i, j)][a[i][j]] = True
go(0)
