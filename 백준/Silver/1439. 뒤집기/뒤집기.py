import sys
input = sys.stdin.readline

def solution():
    n = input().rstrip()
    check = [0,0]
    length = len(n)
    for i in range(1,length):
        if n[i] != n[i-1]:
            check[int(n[i-1])] += 1
    check[int(n[-1])] += 1
    print(min(check))

if __name__ == '__main__':
    solution()