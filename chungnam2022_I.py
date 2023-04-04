a, b = map(int, input().split())
c, d = map(int, input().split())

def prime_list(n):
    prime = [True] * (n)
    m = int(n ** 0.5)
    for i in range(2, m+1):
        if prime[i] == True:
            for j in range(i+i, n, i):
                prime[j] = False
    return [i for i in range(2, n) if prime[i] == True]

ytprime = prime_list(b+1)
ytans = []
for i in ytprime:
    if i >= a:
        ytans.append(i)

yjprime = prime_list(d+1)
yjans = []
for i in yjprime:
    if i >= c:
        yjans.append(i)

between = []
for i in ytans:
    for j in yjans:
        if i==j:
            between.append(i)

between = (set(between))
yjans = set(yjans) - between
ytans = set(ytans) - between

#print(ytans, yjans, between)
if len(between) % 2 ==0:
    start = 'yt'
else:
    start = 'yj'

if start == 'yj':
    if len(yjans) <= len(ytans):
        print('yt')
    else:
        print('yj')
if start == 'yt':
    if len(ytans) <= len(yjans):
        print('yj')
    else:
        print('yt')

# 최선을 다해 -> 겹쳐 있는 소수부터 먼저 부른다
# between이 홀수일때면 yt가 먼저 between을 부른다
# 2 15 17 33