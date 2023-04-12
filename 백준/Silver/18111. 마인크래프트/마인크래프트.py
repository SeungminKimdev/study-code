import sys
input = sys.stdin.readline

def checkSec(high, land):
    sumSec = 0
    tStore = 0
    for i in land:
        num = i-high
        if num < 0:
            sumSec -= num
            tStore += num
        else:
            sumSec += 2 * num
            tStore += num
    return sumSec, tStore

remove = 2
plus = 1

n, m, store = map(int, input().split())
land = []
for _ in range(n):
    land += [int(i) for i in input().split()]

landMax = max(land)
landMin = min(land)
landSum = sum(land)
ansHigh = 0
ansTime = 256 * n * m
for i in range(landMax,landMin-1,-1):
    if landSum + store >= i * n * m:
        sumSec,tStore = checkSec(i,land)
        if store+tStore >= 0:
            if sumSec < ansTime:
                ansTime = sumSec
                ansHigh = i
print(str(ansTime) + " " + str(ansHigh))