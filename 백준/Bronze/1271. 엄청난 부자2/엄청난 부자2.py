import sys
input = sys.stdin.readline

def main():
    m,n = map(int,input().split())
    print(m // n)
    print(m % n)

if __name__ == "__main__":
    main()