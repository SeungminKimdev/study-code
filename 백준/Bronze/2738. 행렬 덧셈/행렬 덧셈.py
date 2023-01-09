import sys
input = sys.stdin.readline

n, m = map(int, input().split())

numList = []
for _ in range(n):
    numList.append(list(map(int,input().split())))
    
for i in range(n):
    temp = list(map(int,input().split()))
    for j in range(m):
        numList[i][j] += temp[j]
        
for i in range(n):
    s = ""
    for j in range(m):
        s += str(numList[i][j]) + " "
    print(s)