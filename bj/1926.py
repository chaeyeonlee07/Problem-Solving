from collections import defaultdict

n, m, v = map(int, input().split())
graph = defaultdict(list)

for i in range(m):
    ind_1, ind_2 = map(int, input().split())
    graph[ind_1].append(ind_2)
    graph[ind_2].append(ind_1)

for i in range(n + 1):
    graph[i] = sorted(graph[i])

visited = [0 for i in range(n+1)]
def dfs(i):
    print(i, end=' ') 
    visited[i] = 1 
    for chil in graph[i]:
        if not visited[chil]:
            dfs(chil)   
dfs(v)
print()

visited = [0 for i in range(n+1)]
queue = []
queue.append(v)
visited[v] = 1 
while queue: 
    x = queue.pop(0)
    print(x, end=' ')
    for j in graph[x]:
        if not visited[j]:
            visited[j] = 1 
            queue.append(j)
print()

    


