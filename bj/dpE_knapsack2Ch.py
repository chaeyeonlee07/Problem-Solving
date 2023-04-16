import sys
input = sys.stdin.readline

n, w = map(int, input().split())

objects = []
sum_val = 0
for _ in range(n):
    x = list(map(int, input().split()))
    sum_val += x[1]
    objects.append(x)


dp = [[float("inf") for i in range(sum_val + 1)] for j in range(n + 1)]

for i in range(n+1):
    dp[i][0] = 0

max_val = 0
for i in range(1, n + 1):
    for j in range(sum_val + 1):
        value = objects[i-1][1]
        weight = objects[i-1][0]
        if j - value >= 0:
            dp[i][j] = min(dp[i-1][j-value] + weight, dp[i-1][j])
            if dp[i][j] <= w and j > max_val:
                max_val = j
        else:
            dp[i][j] = dp[i-1][j]

print(max_val)
