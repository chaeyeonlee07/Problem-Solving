import sys
import heapq
n = int(sys.stdin.readline())
left_heap = []
right_heap = []
a = int(sys.stdin.readline()) 
print(a)
left_heap.append(a)
b = int(sys.stdin.readline())
if a <= b: 
    print(a)
else: 
    print(b)
right_heap.append(b)

# 사이즈를 맞춰 가면서 하나 하나 더해줌.
 
# order from small to large 
# reverse order 
for _ in range(n-2):
    a = int(sys.stdin.readline())
    if len(left_heap) == len(right_heap):
        left_heap.append(-a)
    else:
        right_heap.append(a)
    heapq.heapify(left_heap)
    heapq.heapify(right_heap)
# left heap 은 max heap, right_heap 은 min heap 으로 바꿔줌 
    x = -left_heap[0]
    y =  right_heap[0]
    if x > y: 
        print(y)
    else: 
        print(x)
 
 
     
        
    