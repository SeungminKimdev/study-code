import sys
input = sys.stdin.readline
import itertools

def solution():
    n, m = map(int,input().split())
    numList = list(map(int,input().split()))
    numList.sort()
    nPm = list(itertools.permutations(numList,m))
    for i in nPm:
        print(*i,sep=' ')

if __name__ == '__main__':
    solution()