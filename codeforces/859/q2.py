num_test = int(input())


for _ in range(num_test): 
    sum_even = 0 
    sum_odd = 0 
    num_cand = int(input())
    for i in input().split():
        if int(i) % 2 == 0:
            sum_even += int(i)
        else:
            sum_odd += int(i)
    if sum_even > sum_odd:
        print("yes", end= "\n")
    else:
        print("no", end = "\n")


     
