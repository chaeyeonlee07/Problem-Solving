import sys
from collections import defaultdict
input = sys.stdin.readline()
 

while True:
    n, m = map(int, input.rstrip().split())   
    trees = 0           
    if n == 0 and m == 0 :
        break 
    adj = defaultdict(list)
    for _ in range(m):
        u, v = map(int, input.rstrip().split())         
        adj[u].append(v)
        adj[v].append(u)
    
    vis = [False for _ in range(n+1)]

    def dfs(cur, prev):
        isTree = True 
        for next in adj[cur]:
            if next == prev : # 만약 부모일 경우 건너뜀 
                continue 
            if vis[next]:
                isTree = False 
                continue 
            vis[next] = True 
            dfs(next, cur)
        if isTree: 
            return 1 
        if not isTree:
            return 0 
    for i in range(1,n+1):
        if vis[i] :
            continue
        vis[i] = True 
        isTree = False 
        isTree = dfs(i, -1)
        trees += isTree 
    if not isTree:
        print("No Trees.", end = "\n")
    elif trees == 1: 
        print("There is one tree.", end = "\n")
    else: 
        print("A forest of ", trees, " trees.", end = "\n")




        
        
        

    
