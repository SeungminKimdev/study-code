import sys
input = sys.stdin.readline

N = int(input())
checkNum = 666
num = 0
while N != num:
    if '666' in str(checkNum):
        num += 1
    checkNum += 1
print(checkNum-1)