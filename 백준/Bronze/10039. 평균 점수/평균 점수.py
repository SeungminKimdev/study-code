import sys
input = sys.stdin.readline

ans = 0
for _ in range(5):
    temp = int(input())
    if temp < 40:
        ans += 40
    else:
        ans += temp
print(ans//5)