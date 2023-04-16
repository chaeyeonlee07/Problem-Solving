from logging.handlers import QueueListener
from statistics import variance
import sys
from collections import deque, defaultdict
n, m, v = list(map(int,sys.stdin.readline().split()))
graph = defaultdict(list)
for _ in range(m):
    a, b = list(map(int,sys.stdin.readline().split()))
    graph[a].append(b)
    graph[b].append(a)

for i in range(n):
    graph[i] = sorted(graph[i])

def dfs(node):
    visited[node] = True 
    dfs_visited.append(node)
    for chil in graph[node]:
        if not visited[chil]:
            dfs(chil)
                
                
queue = deque()
visited = [False for _ in range(n+1)]
queue.append(v)  
visited[v] = True 
dfs_visited = []

bfs_visited = []

def bfs(node):
    queue_bfs = deque()
    for i in range(n):
        graph[i] = sorted(graph[i])
    visited_bfs = [False for _ in range(n+1)]
    queue_bfs.append(v)
    visited_bfs[v] = True 
    while queue_bfs:
        x = queue_bfs.popleft()
        bfs_visited.append(x)
        visited_bfs[x] = True 
        for chil in graph[x]:
            if not visited_bfs[chil]:
                queue_bfs.append(chil)
                visited_bfs[chil] = True 
    return bfs_visited

bfs_v = bfs(v)
print(bfs_v)


         
    
