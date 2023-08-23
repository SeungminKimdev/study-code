import sys
input = sys.stdin.readline

def main():
    inNum = list(map(int,input().split()))
    inNum.sort()
    if inNum[2] < inNum[0] + inNum[1] - 1:
        print(sum(inNum))
    else:
        print(2*(inNum[0] + inNum[1]) - 1)
    return

if __name__ == "__main__":
    main()