import sys 
from collections import defaultdict, deque
input = sys.stdin.readline 
n, m = map(int,input().split())
tree = defaultdict(list)
for _ in range(n-1):
    a, b, dis = map(int,input().split())
    tree[a].append([b, dis])
    tree[b].append([a, dis])

distance = []
for _ in range(m):
    q1, q2 = map(int,input().split()) 
    queue = deque()
    queue.append((q1, 0))
    visited = [False for _ in range(n+1)]
    visited[q1] = True 
    while queue: 
        x, dist = queue.popleft()
        if x == q2:
            distance.append(dist)
            break
        else:
            for chil, dis in tree[x]:
                if not visited[chil]: 
                    visited[chil] = True 
                    queue.append((chil, dis + dist))

for i in distance:
    print(i, end = "\n")


    