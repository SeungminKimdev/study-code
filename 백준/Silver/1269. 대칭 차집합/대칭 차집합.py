import sys
input = sys.stdin.readline

def main():
    a,b = map(int,input().split())
    aSet = input().split()
    bSet = input().split()
    ans = len(set(aSet+bSet))
    print((ans - a - b) * 2 + a + b)

if __name__ == "__main__":
    main()