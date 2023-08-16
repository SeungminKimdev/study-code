import sys
input = sys.stdin.readline

def main():
    T = int(input())
    for _ in range(T):
        n = int(input())
        sticker = {0:[0],1:[0]}
        sticker[0] += list(map(int,input().split()))
        sticker[1] += list(map(int,input().split()))
        for i in range(2,n+1):
            sticker[0][i] += max(sticker[1][i-1],sticker[1][i-2])
            sticker[1][i] += max(sticker[0][i-1],sticker[0][i-2])
        print(max(sticker[0][n],sticker[1][n]))
    return

if __name__ == "__main__":
    main()