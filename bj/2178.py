 
from collections import deque 
 
n, m = map(int, input().split()) # n : y, m : x 
table = []
for _ in range(n):
  table.append(list(map(int, input())))

dx = [-1,1,0,0]
dy = [0,0,1,-1]

visited = [[False for _ in range(m)]for i in range(n)]
visited[0][0] = True 
bfs_queue= deque()
bfs_queue.append((0,0))
def dfs(x,y):
    while bfs_queue:
        a = bfs_queue.popleft()
        x, y = a[0], a[1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and table[ny][nx] == 1 and not visited[ny][nx]:
                bfs_queue.append((nx,ny))
                visited[ny][nx] = True 
                table[ny][nx] =  table[y][x] + 1

dfs(0,0)
print(table[n-1][m-1])

                




# def bfs(i, j):
#     count = 0 
#     while bfs_queue:
#         a = bfs_queue.popleft()
#         i, j = a[0], a[1]
#         if i + 1 < n and 0 <= j < m: 
#             if table[i+1][j] == 1 and not visited[i+1][j]:
#                 visited[i+1][j] = True 
#                 bfs_queue.append([i+1, j])
#         if i - 1 >= 0 and 0<= j < m:
#             if table[i-1][j] == 1 and not visited[i-1][j]:
#                 visited[i-1][j] = True 
#                 bfs_queue.append([i-1, j])
#         if j + 1 < m  and 0 <= i <n:
#             if table[i][j+1] == 1:
#                 if not visited[i][j+1]:
#                     visited[i][j+1] = True 
#                     bfs_queue.append([i, j+1])
#         if j - 1 >= 0 and 0 <= i <n : 
#             if table[i][j-1] == 1 and not visited[i][j-1]:
#                 visited[i][j-1] = True 
#                 bfs_queue.append([i, j-1])
#         count = count + 1 
#     return count 
# count = 0  
# print(bfs(0,0))
    
     

    