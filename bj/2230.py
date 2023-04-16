import sys
n, m = map(int, sys.stdin.readline().split())
lst = []
for _ in range(n):
    lst.append(int(sys.stdin.readline()))
lst = sorted(lst)
minimum = float('inf') 
en, st = 0, 0 
for st in range(0, n):
    while en < n and lst[en] - lst[st] < m:
        en += 1 
    if en == n:
        break
    minimum = min(minimum, lst[en]-lst[st])
print(minimum)
