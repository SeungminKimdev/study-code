import sys
input = sys.stdin.readline
from collections import deque

def dfs(start, nList, n, m):
    if len(nList) == m:
        print(*nList,sep=' ')
        return

    for i in range(start,n+1):
        if i not in nList:
            nList.append(i)
            dfs(i+1,nList,n,m)
            nList.pop()

def main():
    n, m = map(int,input().split())
    nList = deque()
    dfs(1,nList,n,m)
    return

if __name__ == '__main__':
    main()