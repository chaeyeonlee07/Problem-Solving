 
import sys
from collections import defaultdict, deque
computers = int(sys.stdin.readline())
lines = int(sys.stdin.readline())
graph = defaultdict(list)
for _ in range(lines):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [False for _ in range(computers+1)]
queue = deque()
queue.append(1) 
visited[1]= True
count = 0 
while queue:
    x = queue.popleft()
    for chil in graph[x]:
        if not visited[chil]:
            queue.append(chil)
            visited[chil] = True 
            count += 1 
print(count)

