
import sys
n = int(sys.stdin.readline())
dp = [0 for _ in range(n+1)] # dp[i] : i 를 가지기 위해 최소한 움직임 
dp[1] = 0
for i in range(2,n+1):
    dp[i] = dp[i-1] + 1 
    if i % 2 == 0 :
        dp[i] = min(dp[i],dp[i//2] +1)  
    if i % 3 == 0 :
        dp[i] = min(dp[i], dp[i//3]+1)
print(dp[n])

 

