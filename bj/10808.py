import sys, string
x = input()

for ch in string.ascii_lowercase:
    ct = 0 
    for x_ch in x:
        
        if ch == x_ch:
            ct += 1 
    print(ct)
            

    