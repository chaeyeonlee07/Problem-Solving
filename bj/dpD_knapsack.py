import sys
input = sys.stdin.readline
n, w  = map(int, input().split())
objects = []
for _ in range(n):
    obj = list(map(int, input().split()))
    objects.append(obj)
dp = [[0 for _ in range(w+1)] for _ in range(n+1)]

for i in range(1,n+1):
    for k in range(w + 1):
        if k-objects[i-1][0] >= 0: 
            dp[i][k] = max(dp[i-1][k-objects[i-1][0]] + objects[i-1][1], dp[i-1][k])
        else: 
            dp[i][k] = dp[i-1][k] 
print(dp[n][k])

    
