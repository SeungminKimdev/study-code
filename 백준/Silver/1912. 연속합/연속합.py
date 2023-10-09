import sys
input = sys.stdin.readline

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int,input().split()))
    maxSum = arr[0]
    sumList = [arr[0]]
    for i in range(1,n):
        sumList.append(max(sumList[i-1] + arr[i],arr[i]))
        maxSum = max(maxSum,sumList[i])
    print(maxSum)