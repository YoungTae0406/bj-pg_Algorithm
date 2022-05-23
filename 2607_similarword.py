#https://www.acmicpc.net/problem/2607
#fail retry
def similar_word(first, other):
    sort_first = sorted(first)
    sort_other = sorted(other)
    if len(first)==len(other):
        same_num = 0
        if sort_first == sort_other:
            return True
        else:
            for a in first:
                print(a, first)
                for b in other:
                    print(b, other)
                    if a==b:
                        same_num+=1
                        other = other.replace(b, " ")
                        break
            if same_num == len(first)-1:
                return True
    else:
        if abs(len(first)-len(other))==1:
            num_min = len(other) if len(first) > len(other) else len(first)
            same_num2 = 0
            for a in first:
                for b in other:
                    if a == b:
                        same_num2 += 1
                        other = other.replace(b, " ")
                        break

            if same_num2 == num_min :
                return True
        else:
            return False
num = int(input())
first_word = input()
word = list()
total_num = 0

for i in range(num-1):
    a = input()
    word.append(a)
for a in word:
    if similar_word(first_word, a) == True:
        total_num += 1

print(total_num)
