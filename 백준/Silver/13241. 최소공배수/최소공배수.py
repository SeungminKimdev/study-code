import sys
input = sys.stdin.readline
import math

if __name__ == '__main__':
    a,b = map(int,input().split())
    print(math.lcm(a,b))