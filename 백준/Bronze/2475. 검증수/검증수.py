import sys

ans = 0
number = list(map(int,sys.stdin.readline().split()))
for i in number:
    ans += (i * i) % 10
    
print(ans % 10)