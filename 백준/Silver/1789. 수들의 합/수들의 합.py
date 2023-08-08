import sys
input = sys.stdin.readline

def main():
    n = int(input())
    i = 1
    ans = 0
    while n >= i:
        ans += 1
        n -= i
        i += 1
    print(ans)
    return

if __name__ == '__main__':
    main()