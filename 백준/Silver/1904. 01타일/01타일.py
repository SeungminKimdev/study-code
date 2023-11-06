import sys
input = sys.stdin.readline

if __name__ == '__main__':
    n = int(input())
    if n < 3:
        print(n)
    else:
        a = 1
        b = 2
        for i in range(2,n):
            temp = (a+b) % 15746
            a = b
            b = temp
        print(b)