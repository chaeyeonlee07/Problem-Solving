n = int(input())
for _ in range(n): 
    len_arr, num_queries = input().split()
    len_arr = int(len_arr)
    num_queries = int(num_queries)
    array = input().split()
    pref_sum = [0 for _ in range(len(array))]
    pref_sum[0] = int(array[0])
    total_sum = int(array[0])
    for i in range(1,len(array)):
        temp = int(array[i]) 
        pref_sum[i] = pref_sum[i] + temp
        total_sum += temp
    for _ in range(num_queries):
        l, r, k = input().split()
        l, r, k = int(l), int(r), int(k)
        print(pref_sum)
        if (total_sum - pref_sum[r-1]-pref_sum[l-1]+ (r-l+1) * k ) % 2 == 0:
            print("No", end = "\n")
        else:
            print("Yes", end = "\n")

 
 