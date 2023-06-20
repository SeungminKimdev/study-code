import sys
input = sys.stdin.readline
import math

def main():
    n = int(input())
    numList = [0,1]
    for i in range(2,n+1):
        minV = 1e9
        j = 1
        while j*j <= i:
            minV = min(minV,numList[i-j*j])
            j += 1
        numList.append(minV+1)
    print(numList[n])
    return

if __name__ == '__main__':
    main()