''''
import sys
sys.setrecursionlimit(int(1e6))
n = int(input())
word = [list(map(str, input())) for _ in range(n)]

number = {}
alphabet = set()
for i in word:
    for j in i:
        alphabet.add(j)

alphabet = list(alphabet)
alphabet.sort()
for i in range(len(alphabet)):
    number[i] = 0

ans = 0
visited = [False for _ in range(10)]
# 각각의 알파벳에 숫자를 부여하고 모든 부여가 끝났으면 단어에 숫자를 대입해서
# 최댓값을 갱신한다.
def recur(idx, avanum):
    global ans
    if idx == len(alphabet):
        #print(number)
        ans_temp = 0
        for i in word:
            wordsum = ''
            for j in i:
                for index, k in enumerate(alphabet):
                    if j == k:
                        wordsum += str(number[index])
            ans_temp += int(wordsum)
            #print(ans_temp)
        ans = max(ans, ans_temp)
        return
    lenn = 9 - len(number)
    for i in range(9, lenn, -1):
        if visited[i] == False:
            number[idx] = i
            visited[i] = True
            recur(idx+1, avanum-1)
            number[idx] = 0
            visited[i] = False
        else:
            continue
#print(number)
recur(0, 9)
print(ans)
'''

n = int(input())
word = [list(map(str, input())) for _ in range(n)]
val_list = []

alphabet = set()
for i in word:
    for j in i:
        alphabet.add(j)
alphabet = list(alphabet)
alphabet.sort()

number = {}
for i in range(len(alphabet)):
    number[alphabet[i]] = 0

for i in word:
    for j in range(len(i)):
        temp = 10 ** (len(i) - j - 1)
        number[i[j]] += temp

#print(number)
for val in number.values():
    if val > 0:
        val_list.append(val)

val_list = sorted(val_list, reverse=True)
ans = 0
for i in range(len(val_list)):
    ans += val_list[i] * (9-i)

print(ans)
