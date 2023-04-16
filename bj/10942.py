import sys
n = int(sys.stdin.readline())
table = [[0]*n for _ in range(n)]
substring = list(map(int,sys.stdin.readline().split()))
num_check = int(sys.stdin.readline())

for i in range(n): 
    table[i][i] = 1 
for i in range(1, n):
    if substring[i-1] == substring[i]:
        table[i-1][i] = 1 
        
for end in range(2, n):
    for start in range(0, end):
        if substring[start] == substring[end] and table[start + 1][end - 1]:
            table[start][end] = 1 
         
for _ in range(num_check): 
    i, j = map(int, sys.stdin.readline().split())
    print(table[i-1][j-1])
 