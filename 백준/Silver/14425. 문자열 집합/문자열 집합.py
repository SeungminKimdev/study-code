import sys
input = sys.stdin.readline

def main():
    n, m = map(int,input().split())
    inList = {}
    for _ in range(n):
        inList[input()] = 1
    ans = 0
    for _ in range(m):
        if input() in inList:
            ans += 1
    print(ans)

if __name__ == "__main__":
    main()