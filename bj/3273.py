from re import I
import sys
n = int(input())
lst = arr = list(map(int, sys.stdin.readline().split()))
x = int(input())
lst = sorted(lst)

l = 0 
r = n-1
count = 0 
while l < r: 
    temp = lst[l] + lst[r]
    if temp == x: 
        count += 1 
        r -= 1 
    if temp < x: 
        l += 1 
    if temp > x: 
        r -= 1
print(count)



