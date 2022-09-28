def myReverse(x):
    return x[::-1]

A,B = map(int,map(myReverse,input().split()))
print(max(A,B))