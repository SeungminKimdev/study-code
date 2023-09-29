import sys
input = sys.stdin.readline
PI = 3.141592

def solution():
    d1 = int(input())
    d2 = int(input())
    print(2*d1 + 2*PI*d2)

if __name__ == '__main__':
    solution()