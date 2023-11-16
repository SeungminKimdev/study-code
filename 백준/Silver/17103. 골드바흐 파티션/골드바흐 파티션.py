import sys
input = sys.stdin.readline

isPrime = [False,False] + [True] * (1000000)
primes = []
for i in range(2,1000001):
    if isPrime[i]:
        primes.append(i)
    for j in range(2*i,1000001,i):
        isPrime[j] = False
        
n = int(input())
for _ in range(n):
    a = int(input())
    ans = 0
    for i in primes:
        if i > a//2:
            break
        if isPrime[a-i]:
            ans += 1
    print(ans)