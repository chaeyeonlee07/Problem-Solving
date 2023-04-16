import sys
input = sys.stdin.readline
n = int(input())
dp = [0] * (n+1)
stairs = list(map(int, input().split()))
dp[1] = 0
dp[2] = abs(stairs[1] - stairs[0])
for i in range(3, n+1):
    dp[i] = min(dp[i-1]+abs(stairs[i-1]-stairs[i-2]), dp[i-2]+abs(stairs[i-1]-stairs[i-3]) ) 
print(dp[n])