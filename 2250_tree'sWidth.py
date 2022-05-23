from collections import defaultdict
import sys
class Node:
    def __init__(self, root, left, right):
        self.root = root
        self.left = left
        self.right = right
        self.leftWidth = 0
        self.height = 1

    def setLeftWidth(self, leftnum):
        self.leftWidth = leftnum

    def setHeight(self, heightnum):
        self.height = heightnum

def traversal(node):
    global cnt
    global ans_height

    ans_height[node.height].append(node.root)
    if node.left != -1:
        tree[node.left].setHeight(node.height + 1)
        traversal(tree[node.left])
    node.setLeftWidth(cnt)
    cnt += 1
    #print(node.root, cnt, node.height)
    if node.right != -1:
        tree[node.right].setHeight(node.height+1)
        traversal(tree[node.right])

n = int(input())
tree = {}
isRoot = [0] * (n+1)
for _ in range(n):
    root, left, right = map(int, sys.stdin.readline().split())
    tree[root] = Node(root, left, right)
    isRoot[root] += 1
    if left != -1:
        isRoot[left] += 1
    if right != -1:
        isRoot[right] += 1
for i in range(1, n+1):
    if isRoot[i] == 1:
        root = i
cnt = 0
ans_height = defaultdict(list)
#print(tree[2].left)
traversal(tree[root])
#print(ans_height)
ans = []

for k in range(len(ans_height)):
    minn = 10**5
    maxx = -1
    if k == 0:
        ans.append(1)
        continue
    for p in ans_height[k+1]:
        minn = min(tree[p].leftWidth, minn)

    for p in ans_height[k+1]:
        maxx = max(tree[p].leftWidth, maxx)
    ans.append(maxx-minn+1)
#print(ans)
m = max(ans)

for idx, a in enumerate(ans):
    if m == a:
        print(idx+1, a)
        break


