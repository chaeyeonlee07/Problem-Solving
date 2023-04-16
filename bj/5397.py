import sys
n = int(sys.stdin.readline())

def listTostring(st):
    s = ""
    for ele in st: 
        s += ele
    return s


for _ in range(n):
    st1 = []
    st2 = [] 
    input = sys.stdin.readline()
    for ch in input: 
        if ch == "<":
            if st1:
                x = st1.pop()
                st2.append(x)
        
        if ch == ">":
            if st2:
                y = st2.pop()
                st1.append(y)
        
        if ch == "-":
            if st1: 
                st1.pop()

        if ch.isalnum():
            st1.append(ch)
    print(str(result).replace('[', '<').replace(']', '>'))