from collections import defaultdict
n, k = list(map(int,input().split()))
thing = [0,0]
dp = [[0] * (k+1) for _ in range(n+1)]
for _ in range(n): 
    a = list(map(int,input().split())) 
    thing.append(a)

for i in range(1,n+1):
    for j in range(k+1):
        w, v = a[i]
        # 현재의 무게를 더해서 초과 하면 넣지 않는다. 
        if j < w: 
            dp[i][j] = dp[i-1][j]
        else:     
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w] + v)
         
print(dp[n][k+1])





























# from collections import defaultdict

# n, k = map(int, input().split())
# thing = [[0,0]]
# d = [[0]*(k+1) for _ in range(n+1)]
# for i in range(n):
#     thing.append(list(map(int, input().split())))

# for i in range(1, n+1):
#     for j in range(1, k+1):
#         w, v = thing[i]
  
#         if j < w: 
#             d[i][j] = d[i-1][j] 
#         else: 
#             d[i][j] = max(d[i-1][j-w] + v, d[i-1][j])  
# print(d[n][k])



 

