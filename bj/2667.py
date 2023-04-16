import sys 
from collections import deque
n = int(sys.stdin.readline()) 
table = []
for _ in range(n):
    table.append(list(map(int, input()))) 

 
visited =  [[False for _ in range (n)]for i in range(n)]
count = 0 
ret = []


def dfs(i,j):
    visited[i][j] = True 
    dx = [-1,1,0, 0]
    dy = [0,0,-1, 1]
    queue = deque()
    area = 1 
    queue.append((i,j))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and table[nx][ny] == 1: 
                queue.append((nx,ny))
                visited[nx][ny] = True 
                area += 1 
    return area 
                

for i in range(n):
    for j in range(n):
        if table[i][j] == 1 and not visited[i][j]: 
            count+=1 
            ret.append(dfs(i,j))

print(count, end = "\n")
ret = sorted(ret)
for i in ret:
    print(i, end =  "\n")
 

