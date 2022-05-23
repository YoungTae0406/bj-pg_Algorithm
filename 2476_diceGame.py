#https://www.acmicpc.net/problem/2476

def dicegame_money(input_dice):
    money = 0
    a, b, c = input_dice
    if a==b and b==c:
        money = 10000 + a * 1000
    elif a==b and b!=c:
        money = 1000 + a * 100
    elif a==c and a!=b:
        money = 1000 + c * 100
    elif b==c and c!=a:
        money = 1000 + c * 100
    elif a!=b and b!=c:
        dice_max = max(a, b, c)
        money = dice_max * 100
    return money

repi = int(input())
input_dice = []
max_money = []
for _ in range(repi):
    input_dice.append(list(map(int, input().split())))

for i in input_dice:
    max_money.append(dicegame_money(i))

print(max(max_money))