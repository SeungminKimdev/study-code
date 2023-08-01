import sys
input = sys.stdin.readline

def main():
    n = int(input())
    ans = 2
    num = 1
    for i in range(n):
        ans += num
        num *= 2
    print(ans**2)

if __name__ == "__main__":
    main()