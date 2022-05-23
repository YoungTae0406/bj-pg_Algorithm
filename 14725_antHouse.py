import sys

class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, string):
        cur = self.root

        for char in string:
            if char not in cur:
                cur[char] = {}
            cur = cur[char]
        cur[0] = True

    def travel(self, level, cur):
        if 0 in cur:
            return
        cur_child = sorted(cur)
        #print(cur_child, level)

        for ch in cur_child:
            print("--" * level + ch)
            self.travel(level + 1, cur[ch])

n = int(input())
trie = Trie()
for _ in range(n):
    temp = list(sys.stdin.readline().split())
    trie.insert(temp[1:])

trie.travel(0, trie.root)
