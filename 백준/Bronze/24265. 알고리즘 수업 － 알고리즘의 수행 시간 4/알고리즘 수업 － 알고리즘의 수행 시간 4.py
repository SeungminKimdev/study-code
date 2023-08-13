import sys
input = sys.stdin.readline

def main():
    n = int(input())
    print(int(n*(n-1) - (n-1)*n/2))
    print(2)

if __name__ == "__main__":
    main()