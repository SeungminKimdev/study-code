import sys
input = sys.stdin.readline
DIVNUM = 1000000007

def facto(n):
    temp = 1
    for i in range(2,n+1):
        temp *= i
        temp %= DIVNUM
    return temp

def pow(n,k):
    if k == 0:
        return 1
    if k == 1:
        return n
    
    temp = pow(n,k//2)
    if k % 2:
        return (temp * temp * n) % DIVNUM
    else:
        return (temp * temp) % DIVNUM

if __name__ == '__main__':
    n,m = map(int,input().split())
    top = facto(n)
    bottom = facto(n-m) * facto(m) % DIVNUM
    print(top * pow(bottom,DIVNUM-2) % DIVNUM)