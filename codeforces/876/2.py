import sys, collections
from collections import defaultdict
n = int(sys.stdin.readline()) 
for _ in range(n): 
    length = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    b = list(map(int, sys.stdin.readline().split()))
    max_a = [1 for _ in range(length)]
    max_b = [1 for _ in range(length)]
    dict_a = defaultdict(lambda:1)
    dict_b = defaultdict(lambda:1)
    dict_a[a[0]] = 1 
    dict_b[b[0]] = 1 
    for i in range(1, length):
        if a[i] == a[i-1]:
            max_a[i] = max_a[i-1] + 1 
            dict_a[a[i]] = max(max_a[i],dict_a[a[i]])
        else:
            dict_a[a[i]] = max(1, dict_a[a[i]])
        
        if b[i] == b[i-1]:
            max_b[i] = max_b[i-1] + 1 
            dict_b[b[i]] = max(max_b[i],dict_b[b[i]])
        else: 
            dict_b[b[i]] = max(1, dict_b[b[i]]) 
         
    max_len = 1
   
    for i in dict_a.keys():
        if i in dict_b: 
            max_len = max(max_len, dict_b[i] + dict_a[i])
        else:
            max_len = max(max_len, dict_a[i])
    for i in dict_b.keys():
        if i in dict_a: 
            max_len = max(max_len, dict_a[i] + dict_b[i])
        else:
            max_len = max(max_len, dict_b[i])
    print(max_len, end = "\n")