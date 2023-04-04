from collections import defaultdict
n = int(input())
node_num = list(map(int, input().split()))
delete_node = int(input())

tree = defaultdict(list)
root = -100
for i in range(n):
    tree[i] = []

for idx, i in enumerate(node_num):
    if i == -1:
        root = idx
    tree[i].append(idx)

#print(tree)

for pnode in tree.keys():
    for k in tree[pnode]:
        if k == delete_node:
            tree[pnode].remove(k)
#print(tree)

cnt = 0
def traversal(root):
    global cnt
    if len(tree[root]) != 0:
        for i in tree[root]:
            traversal(i)
    else:
        cnt += 1

if len(tree[-1]) == 0:
    print(0)
    exit()
else:
    traversal(-1)
print(cnt)



