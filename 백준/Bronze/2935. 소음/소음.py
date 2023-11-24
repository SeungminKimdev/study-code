import sys
input = sys.stdin.readline

a = int(input())
temp = input().rstrip()
b = int(input())
if temp == '+':
    print(a+b)
else:
    print(a*b)