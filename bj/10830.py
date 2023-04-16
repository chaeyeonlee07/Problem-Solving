import sys
 
 
n, k = map(int,input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
matrix2 = matrix

def square(matrix, n, repeat):
    if repeat == 1: 
        for row in range(n):
            for col in range(n):
                for i in range(repeat):
                    matrix[row][col] %= 1000 
        return matrix

    tmp = square(matrix, n//2)
    if repeat % 2 == 0:
        return (multiply(tmp, tmp, repeat//2, n))
    elif n % 2 == 1:
        return (multiply(multiply(tmp, tmp, repeat//2, n),matrix,  n))
             

def multiply(matrixA,matrixB, n):
    ret = [list([0]*k) for k in range(n)] 
    for row in range(n):
        for col in range(n):
            e = 0  
            for i in range(n):
                e += matrixA[row][i] * matrixB[i][col]
            ret[row][col] = e % 1000 
    return ret 

result = square(matrix2, k)
print(result)
 