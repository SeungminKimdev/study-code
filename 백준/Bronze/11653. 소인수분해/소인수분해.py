import sys
input = sys.stdin.readline

def solution():
    n = int(input())
    num = 2
    while n != 1:
        if n%num == 0:
            print(num)
            n = n // num
        else:
            num += 1
if __name__ == '__main__':
    solution()