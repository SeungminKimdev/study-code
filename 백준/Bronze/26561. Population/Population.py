import sys
input = sys.stdin.readline

def main():
    n = int(input())
    for _ in range(n):
        p, t = map(int, input().split())
        print(p + t//4 - t//7)

if __name__ == "__main__":
    main()