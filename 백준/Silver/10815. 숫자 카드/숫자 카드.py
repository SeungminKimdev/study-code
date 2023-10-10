import sys
input = sys.stdin.readline

def main():
    n = int(input())
    numList = list(map(int,input().split()))
    nList = {i:1 for i in numList}
    m = int(input())
    mList = list(map(int,input().split()))
    ans = []
    for i in mList:
        if i in nList:
            ans.append(1)
        else:
            ans.append(0)
    print(*ans,sep=' ')

if __name__ == "__main__":
    main()