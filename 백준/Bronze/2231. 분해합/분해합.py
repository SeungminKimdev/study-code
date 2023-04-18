import sys
input = sys.stdin.readline

def divideSum(num):
    return num + sum(int(i) for i in str(num))

n = input().strip()
numLen = len(n)
n = int(n)
start = n - 9 * numLen
if start < 0:
    start = 1
ans = 0
for i in range(start, n+1):
    if divideSum(i) == n:
        ans = i
        break
print(ans)