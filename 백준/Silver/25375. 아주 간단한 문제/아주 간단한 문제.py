import sys
input = sys.stdin.readline

def main():
    q = int(input())
    for _ in range(q):
        a, b = map(int, input().split())
        print(int(b % a == 0 and b > a))

if __name__ == "__main__":
    main()
