import sys
import math
 
# greedily select the 
n = int(sys.stdin.readline()) 
output = []
for _ in range(n):
    m = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    tot = m + 1 
    b = [] 
    for i in range(m): 
        b.append(tot - arr[i])
    print(*b, end = "\n")
 
        