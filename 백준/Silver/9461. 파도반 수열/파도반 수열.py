import sys
input = sys.stdin.readline

def main():
    n = int(input())
    numList = [1,1,1,2,2]
    for _ in range(n):
        num = int(input())
        for _ in range(5,num):
            numList.append(numList[-1]+numList[-5])
        print(numList[num-1])
    return

if __name__ == '__main__':
    main()