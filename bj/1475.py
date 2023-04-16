import sys
number = int(input())
keys = [0 for _ in range(10)]
while number > 0:
    last = number % 10 
    number //= 10 
    if last == 6: 
        last = 9 
    keys[last] += 1 
if keys[9] % 2 == 0:
    nine = keys[9]// 2 
else:
    nine = keys[9]//2 + 1 
print(max(max(keys[:9]), nine))

    