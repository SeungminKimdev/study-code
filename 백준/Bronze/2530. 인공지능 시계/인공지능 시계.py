import sys

A, B, C = map(int, sys.stdin.readline().split())
D = int(sys.stdin.readline())
T, C = divmod(C+D,60)
R, B = divmod(T+B,60)
A = (A+R) % 24

print("{} {} {}".format(A,B,C))