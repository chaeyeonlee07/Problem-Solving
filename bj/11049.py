from collections import defaultdict
import sys
n = int(sys.stdin.readline()) 
dp = [[0] * n for i in range(n)]
dict = defaultdict(int)
# matrix dictionary
for i in range(n):
    dict[i] = list[map(int, sys.stdin.readline().split())]
# dp 
for _ in range(n):
    