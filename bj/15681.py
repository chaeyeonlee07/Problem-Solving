import sys 
from collections import defaultdict
 
sys.setrecursionlimit(200000)

input = sys.stdin.readline
n, r, q = map(int,input().split())
tree = defaultdict(list)
for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

 
# 해당 정점을 루트로 하는 서브트리에 대한 정점의 수를 계산하는 함수
size = [0 for _ in range(n+1)]
def countSubTree(currNode, parent):
    size[currNode] = 1 
    for chil in tree[currNode]:
        if chil != parent:
            countSubTree(chil, currNode)
            size[currNode] += size[chil]

 
countSubTree(r, -1)


for _ in range(q):
    a = int(input())
    print(size[a], end = "\n")
    

