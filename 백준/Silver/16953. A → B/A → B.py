import sys
input = sys.stdin.readline
from collections import deque

def main():
    a, b = map(int, input().split())
    q = deque()
    q.append((a,1))
    num = 0
    while q:
        num, turn = q.popleft()
        next1 = num*2
        next2 = num*10+1
        if next1 == b or next2 == b:
            num = b
            print(turn+1)
            break
        if next1 < b:
            q.append((next1,turn+1))
        if next2 < b:
            q.append((next2,turn+1))
    if b != num:
        print('-1')
    return

if __name__ == '__main__':
    main()