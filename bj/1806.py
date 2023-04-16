import sys
n,m = map(int, input().split())
lst = list(map(int, input().split()))
en = 0 
temp = lst[0]
min_len = float("inf")
 
if sum(lst) < m:
    print(0)
else:
    for st in range(0,n):
        while en < n and temp < m:
            en += 1 
            if en != n:
                temp += lst[en]
        if en == n:
            break
        min_len = min(min_len, en - st + 1)
        temp -= lst[st]
    print(min_len)

            
            