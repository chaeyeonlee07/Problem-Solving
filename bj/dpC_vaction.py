import sys
 
input = sys.stdin.readline
n = int(input())
dp = [[0 for _ in range(3)] for _ in range(n)]
ben = []
for i in range(n):
    ben.append(list(map(int, input().split())))
dp[0] = ben[0][:]
for i in range(1,n):
    for k in range(3):
        dp[i][k] = max(dp[i-1][(k+1)%3], dp[i-1][(k+2)%3]) + ben[i][k] 
print(max(dp[n-1][0],dp[n-1][1],dp[n-1][2]))
