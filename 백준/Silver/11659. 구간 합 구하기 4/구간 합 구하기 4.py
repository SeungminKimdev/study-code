import sys
input = sys.stdin.readline

def main():
    n, m = map(int,input().split())
    numList = list(map(int,input().split()))
    sumList = [0]
    temp = 0
    for i in numList:
        temp += i
        sumList.append(temp)
        
    for _ in range(m):
        i, j = map(int,input().split())
        print(sumList[j]-sumList[i-1])
    return

if __name__ == '__main__':
    main()