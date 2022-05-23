import sys
class Node(object):
    def __init__(self, key):
        self.key = key
        self.flag = False
        #self.cnt = 0
        self.child = {}

class Trie:
    def __init__(self):
        self.root = Node(None)

    def insert(self, string):
        cur = self.root

        for char in string:
            if char not in cur.child:
                cur.child[char] = Node(char)
            cur = cur.child[char]
        cur.flag = True

    def search(self, string):
        cur = self.root
        ans = 0
        for char in string:
            if cur == self.root:
                ans += 1
                #print(ans, char)

            elif len(cur.child) > 1 or cur.flag:
                ans += 1
                #print(ans, char)
            #print(cur.child)
            cur = cur.child[char]
        return ans

while True:
    try:
        test_case = int(input())
    except:
        exit()
    words = []
    t = Trie()
    for _ in range(test_case):
        temp = str(sys.stdin.readline().rstrip())
        words.append(temp)
        t.insert(temp)
    ansM = 0
    for word in words:
        ansM += t.search(word)
    print("%.2f" % (ansM/test_case))

