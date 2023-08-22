import sys
input = sys.stdin.readline
from itertools import combinations_with_replacement

def solution():
    n, m = map(int,input().split())
    num = list(map(int,input().split()))
    num.sort()
    for i in combinations_with_replacement(num,m):
        print(*list(i),sep=' ')
        
if __name__ == '__main__':
    solution()