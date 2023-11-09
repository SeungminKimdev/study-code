import sys
input = sys.stdin.readline

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int,input().split()))
    rArr = arr[::-1]
    maxDp = [1] * 1001 #증가
    minDp = [1] * 1001 #감소
    for i in range(n):
        for j in range(i):
            if arr[j] < arr[i]:
                maxDp[i] = max(maxDp[i],maxDp[j]+1)
            if rArr[j] < rArr[i]:
                minDp[i] = max(minDp[i],minDp[j]+1)
    ans = 0
    for i in range(n):
        tempSum = maxDp[i] + minDp[n-i-1] -1
        if tempSum > ans:
            ans = tempSum
    print(ans)