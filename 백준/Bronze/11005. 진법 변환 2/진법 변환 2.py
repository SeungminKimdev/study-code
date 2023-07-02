import sys
input = sys.stdin.readline

def main():
    N, B = map(int,input().split())
    ans = ''
    while N > 0:
        N, mod = divmod(N, B)
        if mod > 9:
            ans += chr(55+mod)
        else:
            ans += str(mod)
    print(ans[::-1])
    return

if __name__ == '__main__':
    main()