#https://www.acmicpc.net/problem/2495

def solution(str):
    length = 1
    list_len = []
    for i in range(len(str)-1):
        if str[i] == str[i+1]:
            length+=1
            list_len.append(length)
        else:
            length = 1
    if not list_len:
        return 1
    else:
        return max(list_len)
str1 = input()
str2 = input()
str3 = input()
print(solution(str1))
print(solution(str2))
print(solution(str3))