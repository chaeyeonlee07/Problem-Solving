import sys 
n = int(sys.stdin.readline())
tree = [[] for _ in range(n+1)]
par = [-1] * (n+1)
for _ in range(n):
    a,b = map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)

print(tree)
# def dfs(n):
#     for i in tree[n]:
#         if par[i] == -1 : 
#             par[i] = n 
#             dfs(i)

# dfs(1)
# for i in range(2, n+1):
#     print(par[i])



