import sys
input = sys.stdin.readline
from collections import deque

def main():
    n, m = map(int, input().split())
    board = [0] * 101
    ladder = {}
    for _ in range(n+m):
        u, v = map(int,input().split())
        ladder[u] = v
    q = deque([1])
    move = [6,5,4,3,2,1]
    board[1] = 0
    while q:
        now = q.popleft()
        nowTurn = board[now]
        for i in move:
            next = now + i
            if next in ladder:
                board[next] = -1
                next = ladder[next]
            if next == 100:
                print(nowTurn+1)
                return
            if next < 100 and board[next] == 0:
                board[next] = nowTurn + 1
                q.append(next)
    return

if __name__ == '__main__':
    main()