import sys
 

n = int(sys.stdin.readline())
# if the current element is the minimum Odd, then we cannot subtract with a different odd number to create an even number and the result is positive. 
# def evenCheck(arr, evenDict, oddDict): 
#     # even - even = even
#     # odd - even = odd 
#     # odd - odd =even 
#     # for evenCheck case, the only case that can make ssense is if all numbers are already even. 


def oddCheck(arr, minEven): 
    # for oddCheck case,
    # odd - even = odd 
    # even - odd = odd 
    # check these two cases. 
    for i in range(len(arr)): 
        if arr[i] % 2 == 0 and arr[i] < minOdd: 
            return False 
    return True 

for _ in range(n):
    odd = {} 
    number_of_odds = 0 
    number_of_even = 0 
    even = {}  
    minOdd = float("inf")
    minEven = float("inf") 
    num = int(sys.stdin.readline())
    lst = list(map(int, sys.stdin.readline().split()))
    len_lst = len(lst)
    for i in range(num):
        if lst[i] % 2 == 1: 
            minOdd = min(minOdd, lst[i])
            odd[i] = lst[i]
            number_of_odds +=1 

        else:
            minEven = min(minEven, lst[i]) 
            even[i] = lst[i]
            number_of_even +=1  
    if number_of_odds == len_lst or number_of_even == len_lst or oddCheck(lst, minEven): 
        print("YES", end = "\n")
    else:
        print("NO", end = "\n")
 
 
 
 


        