from cmath import inf
import sys
n = int(sys.stdin.readline())
dp = [1] * n
a = list(map(int, sys.stdin.readline().split()))

for i in range(len(a)):
    for j in range(i):
        if a[j] < a[i]:
            dp[i] = max(dp[i], dp[j] + 1 )
            
     