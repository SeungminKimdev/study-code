import sys
input = sys.stdin.readline

def main():
    a,b,c = map(int,input().split())
    print(pow(a,b,c))
    return

if __name__ == '__main__':
    main()