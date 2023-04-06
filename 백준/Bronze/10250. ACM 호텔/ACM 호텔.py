import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    h, w, n = map(int, input().split())
    xx, yy = divmod(n, h)
    if yy == 0:
        yy = h
    else:
        xx += 1
    print(yy * 100 + xx)