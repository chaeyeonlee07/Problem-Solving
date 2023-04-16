import sys
input = sys.stdin.readline

n, W = map(int, input().split())




# w = [0] * n
# v = [0] * n
# for i in range(n):
#     wi, vi = map(int, input().split())
#     w[i] = wi
#     v[i] = vi

# V = sum(v)
# dp = [[float("inf") for i in range(V+1)] for j in range(n+1)]

# for i in range(n):
#     dp[i][0] = 0

# for i in range(1, n+1):
#     for j in range(1, V+1):
#         if j - v[i-1] >= 0:
#             dp[i][j] = min(dp[i-1][j], dp[i-1][j-v[i-1]] + w[i-1])
#         else:
#             dp[i][j] = dp[i-1][j]

# ans = 0
# for i in range(V+1):
#     if dp[n][i] <= W:
#         ans = max(ans, i)
# print(ans)