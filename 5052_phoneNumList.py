import sys
test_case = int(input())
while test_case:
    n = int(input())
    phNList = [sys.stdin.readline().rstrip() for _ in range(n)]

    phNList.sort()
    #print(phNList)

    for idx in range(len(phNList) - 1):
        if phNList[idx] in phNList[idx+1]:
            print("NO")
            break
    else:
        print("YES")
    test_case -= 1
