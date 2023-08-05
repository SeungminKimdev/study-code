import sys
input = sys.stdin.readline

def main():
    n, k = map(int,input().split())
    check = 0
    ans = 0
    for i in range(1,n+1):
        if n % i == 0:
            check += 1
        if check == k:
            ans = i
            break
    if check == k:
        print(ans)
    else:
        print(0)

if __name__ == "__main__":
    main()