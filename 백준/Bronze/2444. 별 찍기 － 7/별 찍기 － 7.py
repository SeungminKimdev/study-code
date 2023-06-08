import sys
input = sys.stdin.readline

def star():
    n = int(input())
    for i in range(1, n):
        print(' '*(n-i) + '*'*(2*i-1))
    for i in range(n, 0, -1):
        print(' '*(n-i) + '*'*(2*i-1))

if __name__ == "__main__":
    star()