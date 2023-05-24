import sys, collections
from collections import defaultdict
numCases = int(sys.stdin.readline())

for _ in range(numCases): 
    n, k = list(map(int,sys.stdin.readline().split()))
    a = list(map(int,sys.stdin.readline().split())) 
    b = list(map(int,sys.stdin.readline().split())) 
    
    # sort 
    sorted_b = sorted(b)

    # sort 
    sorted_a = sorted(a)

    dict = defaultdict(list)
    for i in range(len(sorted_b)):
        dict[sorted_a[i]].append(sorted_b[i])
    
    ans = []
    for j in range(len(sorted(a))):
        ans.append(dict[a[j]][-1])
        dict[a[j]].pop(-1)
    
    print(* ans, end = "\n")