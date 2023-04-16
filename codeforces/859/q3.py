from collections import defaultdict

 
num_test = int(input())
for _ in range(num_test):
    str_len = int(input())
    seen = defaultdict(int)
    string = str(input())
    seen[string[0]] = 0 
    count = 0 
    for i in range(1,str_len):
        if string[i] in seen:
            if i%2 != seen[string[i]] % 2:
                if count == 0 : 
                    print("no", end = "\n")
                count += 1 
        else:
            seen[string[i]] = (seen[string[i-1]] + 1) % 2 
    if count == 0:
        print("yes", end = "\n" )


            

     