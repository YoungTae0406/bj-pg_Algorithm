#https://www.acmicpc.net/problem/2477

basemelon = int(input())
length = {'1': [], '2': [], '3':[], '4':[]}

rect1 = 0
rect2 = 0
#1 east 2 west 3 south 4 north
for _ in range(6):
    direction, sidelength = map(int, input().split())
    direction = str(direction)
    length[direction].append(sidelength)

if len(length['3']) > len(length['4']):
    if len(length['1']) > len(length['2']):
        rect1 = length['4'][0] * length['2'][0]
        rect2 = length['3'][1] * length['1'][0]

if len(length['3']) > len(length['4']):
    if len(length['2']) > len(length['1']):
        rect1 = length['4'][0] * length['1'][0]
        rect2 = length['3'][1] * length['2'][0]

if len(length['4']) > len(length['3']):
    if len(length['1']) > len(length['2']):
        rect1 = length['3'][0] * length['2'][0]
        rect2 = length['4'][1] * length['1'][0]

if len(length['4']) > len(length['3']):
    if len(length['2']) > len(length['1']):
        rect1 = length['3'][0] * length['1'][0]
        rect2 = length['4'][1] * length['2'][0]

print(basemelon*rect1 - basemelon*rect2)



