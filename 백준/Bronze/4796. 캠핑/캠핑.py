import sys
input = sys.stdin.readline

def main():
    num = 1
    while 1:
        l,p,v = map(int,input().split())
        if l == 0 and p == 0 and v == 0:
            break
        a,b = divmod(v,p)
        if l < b:
            b = l
        ans = a*l + b
        print(f'Case {num}: {ans}')
        num += 1

if __name__ == "__main__":
    main()