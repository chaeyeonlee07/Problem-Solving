import sys
from collections import defaultdict, deque 
ppl = int(sys.stdin.readline())
a, b = map(int, sys.stdin.readline().split())
lines = int(sys.stdin.readline())
graph = defaultdict(list)
visited = [False for _ in range(ppl+1)]
res = [0] * (ppl+1)
for _ in range(lines):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)
 
def bfs(node):
    queue = deque()
    visited[node] = True 
    queue.append(node) 
    while queue:
        y = queue.popleft()
        for per in graph[y]:
            if not visited[per]:
                visited[per] = True 
                queue.append(per)
                res[per]=res[y]+1
     
bfs(a)
if res[b]!= 0:
    print(res[b])
else:
    print(-1)
    



