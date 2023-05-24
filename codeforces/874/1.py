import sys
numCases = int(sys.stdin.readline()) 
for _ in range(numCases): 
    n = int(sys.stdin.readline())
    str = sys.stdin.readline()
    count = 0 
    dict = []
    for i in range(n-1):
        if str[i] + str[i+1] not in dict:
            dict.append(str[i] + str[i+1])
            count += 1 
    print(count, end = "\n")
