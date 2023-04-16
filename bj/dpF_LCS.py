import sys
input = sys.stdin.readline

s1 = input().strip()
s2 = input().strip()

# dp = [[0 for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]

# for i in range(1, len(s1) + 1):
#     for j in range(1, len(s2) + 1):
#         if s1[i-1] == s2[j-1]:
#             dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]+1)
#         else:
#             dp[i][j] = max(dp[i-1][j], dp[i][j-1])
# print(dp[-1][-1])



dp = [[0 for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]

for i in range(len(s1) + 1):
    dp[i][0] = 0 

for j in range(len(s2) + 1):
    dp[0][j] = 0 

prev = {}
for i in range(1, len(s1) + 1):
    for j in range(1, len(s2) + 1):
        if s1[i-1] == s2[j-1]: 
            dp[i][j] = max(dp[i-1][j-1] + 1, dp[i-1][j], dp[i][j-1])
            if dp[i][j] == dp[i-1][j-1] + 1:
                prev[(i, j)] = (i-1, j-1)
            elif dp[i][j] == dp[i-1][j]:
                prev[(i, j)] = (i-1, j)
            else:
                prev[(i, j)] = (i, j-1)
        else: 
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            if dp[i][j] == dp[i-1][j]:
                prev[(i, j)] = (i-1, j)
            else:
                prev[(i, j)] = (i, j-1)

i, j = len(s1), len(s2)
ans = ""
while (i, j) in prev:
    if prev[(i, j)] == (i-1, j-1):
        ans += s1[i-1]
    i, j = prev[(i, j)]
print(ans[::-1])        

# print(dp)
# print(dp[len(s1)][len(s2)])