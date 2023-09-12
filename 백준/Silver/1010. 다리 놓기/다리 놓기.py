import sys
input = sys.stdin.readline
from math import comb

def solution():
    n = int(input())
    for _ in range(n):
        a,b = map(int,input().split())
        print(comb(b,a))
        
if __name__ == '__main__':
    solution()