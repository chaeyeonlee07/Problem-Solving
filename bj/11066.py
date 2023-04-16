import sys
n = int(sys.stdin.readline())
 
for _ in range(n):
    k = int(sys.stdin.readline())
    files = list(map(int, sys.stdin.readline().split()))
    dp = [[0]*k for _ in range(k)]
    #dp[a][b] 는 a 부터 b 까지의 파일을 압축하는데 드는 최소 비용.
    subSum = {-1 : 0} #files 의 어떤 인덱스 까지의 연속합.
    #subSum 을 채워 준다.
    for j in range(k):
        subSum[j] = subSum[j-1] + files[j]
    for size in range(1,k): # size 크기로 묶은 그룹들의 minimum cost 구하기 
        for start in range(k-1): # 그룹 시작의 인덱스의 범위는 0 부터 k-2 
            end = start + size 
            if end >= len(files):
                break
            result = float("inf")
            for cut in range(start, end):
                result = min(result, dp[start][cut] + dp[cut+1][end]+subSum[end] - subSum[start - 1])
            
            dp[start][end] = result
    print(dp[0][-1])