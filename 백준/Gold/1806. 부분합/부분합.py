import sys
input = sys.stdin.readline

N, S = map(int,input().split())
seq = list(map(int,input().split()))
low = high = 0
sumNum = seq[0]
len = N+1
while True:
    if sumNum < S:
        high += 1
        if high == N:
            break
        sumNum += seq[high]
    else:
        sumNum -= seq[low]
        len = min(len,high-low+1)
        low += 1
if len == N+1:
    print('0')
else:
    print(len)