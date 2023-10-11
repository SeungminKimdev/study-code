import sys
input = sys.stdin.readline

def main():
    numList = list(map(int,input().split()))
    numList.sort()
    print(*numList, sep=' ')
    
if __name__ == "__main__":
    main()