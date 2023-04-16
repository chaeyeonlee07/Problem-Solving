n = int(input())
for i in range(n): 
    len_arr, num_queries = input().split()
    len_arr = int(len_arr)
    num_queries = int(num_queries)
    array = input().split()
    total_sum = 0
    for i in range(len_arr):
        total_sum += array[i]
    for _ in range(num_queries):
        l, r, k = input().split()
        l, r, k = int(l), int(r), int(k)
        if (total_sum - (r-(l-1))*k) % 2 == 0:
            print("yes", end = "\n")

 
 