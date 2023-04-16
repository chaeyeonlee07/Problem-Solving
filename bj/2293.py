n, k = map(int, input().split())  # n: 동전의 종류, k: 가치의 합
c = []
for i in range(n):
    c.append(int(input()))
dp = [10001 for _ in range(k+1)]
dp[0] = 0
for i in range(k+1):
    for j in c:
        if i >= j:
            dp[i] = min(dp[i], dp[i-j] + 1)
if dp[k] == 10001: print(-1)
else: print(dp[k])
    