import itertools as it
N = int(input())
a = list(it.permutations(range(1, N+1)))
a = sorted(a)
for i in a:
    for j in i:
        print(j, end = " ")
    print()