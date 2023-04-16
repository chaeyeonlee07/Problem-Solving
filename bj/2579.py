import sys 
n = int(sys.stdin.readline())
points = [0 for _ in range(n)]
for i in range(n):
    points[i] = int(sys.stdin.readline())
dp = [[0 for _ in range(3)] for _ in range(n)]
dp[0][0] = 0 
dp[1][1] = points[0]
dp[2][1] = points[1]
dp[2][2] = points[0] + points[1]
for i in range(3,n+1):
    dp[1][i] =max (dp[1][i-2], dp[2][i-2]) + points[i-1]# 2번 전꺼는 밟음 
    dp[2][i] = dp[1][i-1] + points[i-1]
print(max(dp[1][n], dp[2][n]))