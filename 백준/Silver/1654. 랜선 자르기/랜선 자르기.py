import sys
input = sys.stdin.readline

def cutting(numList, cut):
    return sum(i//cut for i in numList)

def binary_search_max(numList):
    low = 0
    high = len(numList) - 1
    while low < high:
        mid = (low + high) // 2
        if numList[mid] < numList[mid+1]:
            low = mid + 1
        else:
            high = mid
    return numList[low]

def cutLan(numList, N):
    low = 1
    high = binary_search_max(numList)
    ans = 0
    while low <= high:
        mid = (low + high) // 2
        cutNum = cutting(numList,mid)
        if cutNum >= N:
            low = mid + 1
            ans = mid
        else:
            high = mid - 1
    print(ans)

K, N = map(int, input().split())
numList = [int(input()) for _ in range(K)]
cutLan(numList, N)