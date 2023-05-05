import sys
input = sys.stdin.readline

def checknum(a, b):
    ans = 0
    num = a
    while num % b == 0 and num != 0:
        ans += 1
        num = int(num / b)
    return ans

n = int(input())
two = 0
fiv = 0
for i in range(1,n+1):
    two += checknum(i,2)
    fiv += checknum(i,5)

print(min(two,fiv))