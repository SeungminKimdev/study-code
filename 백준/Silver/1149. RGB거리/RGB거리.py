import sys
input = sys.stdin.readline

def main():
    n = int(input())
    before = list(map(int,input().split()))
    for _ in range(n-1):
        r, g, b = map(int,input().split())
        tempList = [0,0,0]
        tempList[0] = r + min(before[1],before[2])
        tempList[1] = g + min(before[0],before[2])
        tempList[2] = b + min(before[0],before[1])
        before = tempList
    print(min(before))
    return

if __name__ == '__main__':
    main()