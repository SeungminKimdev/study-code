import sys
input = sys.stdin.readline
from collections import deque

def solution():
    n, m = map(int,input().split())
    ans = deque()
    def dfs(num):
        if len(ans) == m:
            print(*ans,sep=' ')
            return
        for i in range(num,n+1):
            ans.append(i)
            dfs(i)
            ans.pop()
    dfs(1)
    return

if __name__ == '__main__':
    solution()