import sys
x = int(sys.stdin.readline())
f = list(map(int,sys.stdin.readline().split()) )
dist = len(f)
n = int(sys.stdin.readline())

def find_cycle(f, x):
    a = x 
    count = 1 
    while f[x] != a: 
        count += 1
        x = f[x]
    return count 
for _ in range(n):
    a, x = map(int,sys.stdin.readline().split())
    if a <= dist:
        for _ in range(a):
           x = f[x]
           print(x, end = "\n")
        print(x)
    elif a > dist:
        cycle = find_cycle(f,x)
        for _ in range(n % cycle):
            x = f[x]
        print(x)



           
       

   