import sys
input = sys.stdin.readline

def main():
    password = {}
    m, n = map(int,input().split())
    for _ in range(m):
        site, passW = input().split()
        password[site] = passW
    for _ in range(n):
        site = input().rstrip()
        print(password[site])
    return

if __name__ == '__main__':
    main()