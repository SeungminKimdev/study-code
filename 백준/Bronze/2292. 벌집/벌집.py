import sys
input = sys.stdin.readline

n = int(input())
num = 1
ans = 1
while num < n:
    ans += 1
    num += (ans-1) * 6
print(ans)