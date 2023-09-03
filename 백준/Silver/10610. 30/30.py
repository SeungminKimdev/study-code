import sys
input = sys.stdin.readline

def solution():
    n = input().rstrip()
    if '0' not in n:
        print(-1)
    else:
        numList = list(map(int,list(n)))
        if sum(numList) % 3 != 0:
            print(-1)
        else:
            numList.sort(reverse=True)
            print(*numList,sep='')

if __name__ == '__main__':
    solution()