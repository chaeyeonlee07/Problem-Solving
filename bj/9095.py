import sys
a = int(sys.stdin.readline())
for _ in range(a):
    n = int(sys.stdin.readline())
    d = [0 for _ in range (n+1)]
    d[1], d[2], d[3] = 1, 2, 4   
    for i in range(4, n+1):
        d[i] = d[i-1] + d[i-2] + d[i-3]
    print(d[n], end = "\n")
