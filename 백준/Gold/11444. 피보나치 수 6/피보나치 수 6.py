import sys
input = sys.stdin.readline
DIVNUM = 1000000007

def dot(a, b):
    matrix = [[0,0],[0,0]]
    matrix[0][0] = (a[0][0]*b[0][0] + a[0][1]*b[1][0]) % DIVNUM
    matrix[0][1] = (a[0][0]*b[0][1] + a[0][1]*b[1][1]) % DIVNUM
    matrix[1][0] = (a[1][0]*b[0][0] + a[1][1]*b[1][0]) % DIVNUM
    matrix[1][1] = (a[1][0]*b[0][1] + a[1][1]*b[1][1]) % DIVNUM
    return matrix

def matrixP(matrix, n):
    if n == 1:
        return matrix
    elif n % 2 == 0:
        halfMat = matrixP(matrix,n//2)
        return dot(halfMat,halfMat)
    else:
        halfMat = matrixP(matrix,(n-1)//2)
        return dot(dot(halfMat,halfMat),matrix)

def fib(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    
    matrix = [[1,1],[1,0]]
    ansMatrix = matrixP(matrix,num-1)
    return ansMatrix[0][0]

def solution():
    n = int(input())
    print(fib(n))
    
if __name__ == '__main__':
    solution()