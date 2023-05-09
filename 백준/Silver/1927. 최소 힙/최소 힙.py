import sys
input = sys.stdin.readline
from queue import PriorityQueue

n = int(input())
q = PriorityQueue(maxsize=n)
for _ in range(n):
    temp = int(input())
    if temp == 0:
        if q.qsize() == 0:
            print('0')
        else:
            print(q.get())
    else:
        q.put(temp)