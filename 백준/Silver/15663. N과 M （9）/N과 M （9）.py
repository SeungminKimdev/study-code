import sys
input = sys.stdin.readline
from itertools import permutations

def solution():
    n, m = map(int,input().split())
    num = list(map(int,input().split()))
    ans = list(set(list(permutations(num,m))))
    ans.sort()
    for i in ans:
        print(*list(i),sep=' ')
        
if __name__ == '__main__':
    solution()