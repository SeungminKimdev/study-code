import sys
input = sys.stdin.readline

n = int(input())
fib = [[0,0] for _ in range(41)]
fib[0][0] = 1
fib[1][1] = 1

for i in range(2,41):
    fib[i][0] = fib[i-1][0] + fib[i-2][0]
    fib[i][1] = fib[i-1][1] + fib[i-2][1]

for _ in range(n):
    inputNum = int(input())
    print(*fib[inputNum])