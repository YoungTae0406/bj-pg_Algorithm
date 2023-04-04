n, m = map(int, input().split())
truthknow = list(map(int, input().split())) # 번호는 1부터 n
party = []

# 각 파티의 인원끼리 union을 하고 진실을 아는 사람과 각각의 사람하고
# find를 진행해 연결이 안되는 파티의 개수를 찾아낸다.
node_root = [0] + [i for i in range(1, n+1)]

def find(x):
    if node_root[x] != x:
        node_root[x] = find(node_root[x])
    return node_root[x]

def union(a, b):
    roota = find(a)
    rootb = find(b)
    if roota < rootb:
        node_root[rootb] = roota
    else:
        node_root[roota] = rootb


for _ in range(m):
    inp = list(map(int, input().split()))
    party_num = inp[0]
    temp_party = []
    temp_party.extend(inp[1:])
    for tp in range(len(temp_party)-1):
        a = temp_party[tp]
        b = temp_party[tp+1]
        union(a, b)
    party.append(temp_party)
#print(party)

if len(truthknow) == 1:
    print(m)
    exit()

#print(node_root)
for tk in range(1, len(truthknow)):
    truth_human = truthknow[tk]
    roottruth = find(truth_human)
    for i in range(1, n+1):
        if truthknow[tk] == i:
            continue
        root_temp = find(i)
        #print(i, root_temp)
        if roottruth == root_temp:
            truthknow.append(i)

#print(node_root)
#print(truthknow)
party_flag = [False] * m
for i in range(1, len(truthknow)):
    th = truthknow[i]
    for p in range(len(party)):
        if th in party[p]:
            party_flag[p] = True

#print(party_flag)
ans = 0
for i in party_flag:
    if i == False:
        ans += 1
print(ans)