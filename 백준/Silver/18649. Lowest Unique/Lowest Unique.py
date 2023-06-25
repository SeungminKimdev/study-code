import sys
input = sys.stdin.readline

def main():
    n, k, m = map(int,input().split())
    while m:
        m -= 1
        temp = ""
        for i in range(1,k):
            temp += str(i)
            temp += " "
        temp += str(k)
        print(temp, flush=True)
        input()
    return

if __name__ == '__main__':
    main()