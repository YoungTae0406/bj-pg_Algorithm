import itertools

def combination(arr, r):
    arr = sorted(arr)

    def generate(chosen):
        if len(chosen) == r:
            print(chosen)
            return
        start = arr.index(chosen[-1]) + 1 if chosen else 0
        print(start)
        for nxt in range(start, len(arr)):
            chosen.append(arr[nxt])
            generate(chosen)
            chosen.pop()
    generate([])

combination('ABCDE', 2)

result = list(itertools.combinations(['A', 'B','C','D','E'], 2))
print("count = ", len(result))
print(result)