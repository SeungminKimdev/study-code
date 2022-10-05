def search(tmpList, size, sNum) -> int:
    minNum = 0
    middle = size // 2
    maxNum = size
    while minNum < maxNum:
        if tmpList[middle] == sNum:
            return 1
        elif tmpList[middle] < sNum:
            minNum = middle + 1
            middle = (minNum + maxNum) // 2
        else:
            maxNum = middle
            middle //= 2
    return 0
N = int(input())
ans = sorted(list(map(int,input().split())))
M = int(input())
numList = list(map(int,input().split()))
for i in numList:
    print(search(ans,N,i))