import sys
hashmap = dict()
n = int(sys.stdin.readline())
for i in range(n):
    a, b = sys.stdin.readline().split()
    if b == "enter": 
        hashmap[a] = True
    else:
        hashmap.pop(a)
x= sorted(hashmap.keys())[::-1]
for i in x:
    print(i, end ="\n")