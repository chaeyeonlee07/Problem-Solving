import sys 
n = int(sys.stdin.readline()) 
numbers = list(map(int, sys.stdin.readline().split()))
dp = [0 for _ in range(n)]
trace = [[] for _ in range(n)]
maximum = 0 
for i in range(n):
    for j in range(i):
        if numbers[j] < numbers[i]: 
            if dp[j] > dp[i] :
                dp[i] = dp[j]
                maximum = j
    if maximum < n and maximum != i: 
        for elem in trace[maximum]:
            trace[i].append(elem)
        
    dp[i] += 1 
    maximum = i + 1 
    trace[i].append(numbers[i]) 
print(max(dp))
for i in range(n):
    if len(trace[i]) == max(dp):
        print(*trace[i]) 
        break