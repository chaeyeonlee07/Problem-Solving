import sys
from collections import defaultdict
# 1. 그래프를 만들어 준다 
# 2. starting from 1, dfs. do the cycle twice, 
# 3. if that person is not already visited, then we add them to the count 

# 1. Make the graph 
input = sys.stdin.readline
n = int(input())
m = int(input())
friends = defaultdict(list)
for _ in range(m):
    a, b = map(int, input().split())
    friends[a].append(b)
    friends[b].append(a)
 
# We start from 1, we do dfs
visited = [False] * (n+1)
visited[1] = True 
def dfs(node, count):
    if count < 2: 
        for fr in friends[node]:
            visited[fr] = True  
            dfs(fr, count + 1)
dfs(1, 0)
print(sum(visited)- 1)


            

    

