import sys
input = sys.stdin.readline

L = int(input())
alp = str(input())

ans = 0
for i in range(L):
    ans += (ord(alp[i])-96) * (31 ** i)
print(ans)