import sys
input = sys.stdin.readline

n = int(input())
fib = [0,1,1]
for num in range(3,1500001):
    fib.append((fib[num-2] + fib[num-1]) % 1000000)
print(fib[n%1500000])