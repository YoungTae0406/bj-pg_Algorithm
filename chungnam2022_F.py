yongtae, yujin = map(int, input().split())

while True:
    yujin += yongtae
    if yujin >= 5:
        print('yt')
        break
    yongtae += yujin
    if yongtae >= 5:
        print('yj')
        break
