import sys
input = sys.stdin.readline

def main():
    a, b = map(int,input().split())
    print(abs(a-b))
    return

if __name__ == "__main__":
    main()