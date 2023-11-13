import sys
input = sys.stdin.readline

n, b = map(int,input().split())

def arrMul(arr1,arr2):
    returnArr = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                returnArr[i][j] += arr1[i][k] * arr2[k][j]
            returnArr[i][j] %= 1000
    return returnArr

def pow(arrT,k):
    if k == 1:
        for i in range(n):
            for j in range(n):
                arrT[i][j] %= 1000
        return arrT
    temp = pow(arrT,k//2)
    if k % 2 == 0:
        return arrMul(temp,temp)
    else:
        return arrMul(arrMul(temp,temp),arrT)

arr = []
for _ in range(n):
    arr.append(list(map(int,input().split())))

answer = pow(arr,b)
for i in answer:
    print(*i,sep=' ')