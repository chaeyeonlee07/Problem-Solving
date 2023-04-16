import sys
n = int(sys.stdin.readline())

# 에라토스테네스의 체 
a = [False, False] + [True] * (n-1)
prime_num = []

for i in range(2, n+1):
    if a[i]:
        prime_num.append(i)
        for j in range(2*i, n+1, i):
            a[j] = False 
en = 0 
temp = prime_num[0]
count = 0 
for st in range(0, len(prime_num)): 
    while en < len(prime_num) and temp < n: 
        en += 1 
        if en != len(prime_num):
            temp += prime_num[en]
        if en == n: 
            break
    if temp == n: 
        count += 1 
    temp -= prime_num[st]
print(count)

    
    
 