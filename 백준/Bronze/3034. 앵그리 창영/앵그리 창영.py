import sys
input = sys.stdin.readline

def solution():
    n,w,h = map(int,input().split())
    for _ in range(n):
        check = int(input())
        if check*check > w**2 + h**2:
            print('NE')
        else:
            print('DA')

if __name__ == '__main__':
    solution()