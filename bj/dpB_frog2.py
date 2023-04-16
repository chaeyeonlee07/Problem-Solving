import sys 
input = sys.stdin.readline
n, k = map(int,input().split())
stairs = list(map(int, input().split()))
dp = [0] * n
dp[0] = 0
for i in range(1, n):
    dp[i] = dp[i-1] + abs(stairs[i]-stairs[i-1])
    if k >= 2:
        for j in range(2,k+1):
            if i-j >= 0:
                dp[i] = min(dp[i],  dp[i-j] + abs(stairs[i]-stairs[i-j]))
print(dp[n-1])