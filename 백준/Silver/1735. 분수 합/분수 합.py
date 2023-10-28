import sys
input = sys.stdin.readline
import math

if __name__ == '__main__':
    a,b = map(int,input().split())
    c,d = map(int,input().split())
    a1 = a*d + c*b
    b1 = b*d
    temp = math.gcd(a1,b1)
    print(f'{int(a1/temp)} {int(b1/temp)}')