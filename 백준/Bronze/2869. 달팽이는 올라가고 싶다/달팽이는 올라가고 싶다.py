import sys
N, M, V = map(int, sys.stdin.readline().split())
dayDis = N - M
day, last = divmod((V-N),dayDis)
if last != 0:
    day += 1
print(day+1)