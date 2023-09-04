import sys
input = sys.stdin.readline

def main():
    while 1:
        a,b = map(int,input().split())
        if a == 0 and b == 0:
            break
        if a > b:
            print('Yes')
        else:
            print('No')

if __name__ == "__main__":
    main()