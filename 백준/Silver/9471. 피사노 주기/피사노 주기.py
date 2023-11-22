import sys
input = sys.stdin.readline

p = int(input())
for _ in range(p):
    N, m = map(int,input().split())
    fib = [0,1,1]
    n=3
    while True:
        fib.append((fib[n-2] + fib[n-1]) % m)
        if fib[n-1] % m == 0 and fib[n] % m == 1:
            break
        n += 1
    print(N,n-1,sep=' ')